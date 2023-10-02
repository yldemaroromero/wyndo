from website.models import Item
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
import logging
logger = logging.getLogger('django')
from .utils.helpers import get_type_of_object, get_url
from django.conf import settings
from .services.clover import get_token, get_data, create_object, update_object, delete_object

def main(request):
  client_id = request.GET.get('client_id')
  code = request.GET.get('code')

  response_body = get_token(client_id, code)

  if response_body is not None:
    logger.info(response_body["access_token"])

  return render(request, "clover.html")

def action(type, data):
  try:
    match type:
      case 'CREATE':
        logger.info('CREATE')
        res = create_object(data)
        logger.info(res)
      case 'UPDATE':
        object = Item.objects.filter(itemId=data.get('id'))

        if object.exists():
          logger.info('UPDATE')
          update_object(object, data)
        else:
          logger.info('CREATE')
          res = create_object(data)
          logger.info(res)
      case 'DELETE':
        logger.info('DELETE')
        object = Item.objects.filter(itemId=data.get('id'))
        if object.exists():
          id = object[0].pk
          delete_object(id)
      case _:
        logger.info('none')
  except Exception as e:
    logger.error(e)  

@api_view(['POST'])
def webhook(request):
  logger.info('clover webhook')
  body = JSONParser().parse(request)
  
  if body.get('verificationCode', None) is not None:
    logger.info(body)
  else:
    merchants = body.get("merchants")
    logger.info(merchants)
    for merchant in merchants.get(settings.MERCHANT_ID):
      merchant_type_action = merchant.get("type")
      merchant_object_id = merchant.get("objectId")
      [object_type, object_id] = str(merchant_object_id).split(':')
      url = get_url(object_type, object_id)
      logger.info('Action: {}, Object type: {}'.format(merchant_type_action, get_type_of_object(object_type)))
      
      if merchant_type_action in 'DELETE':
        action(merchant_type_action, { 'id': object_id})
      else: 
        res = get_data(url)
        logger.info(res)
        action(merchant_type_action, res)

  return render(request, "clover.html")



