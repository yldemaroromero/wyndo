from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from .services.square_up import get_token, get_data
import logging
logger = logging.getLogger('django')

def main(request):
  code = request.GET.get('code')

  response_body = get_token(code)

  if response_body is not None:
    logger.info(response_body.get("access_token"))

  return render(request, "square_up.html")

@api_view(['POST'])
def webhook(request):
  logger.info('square up webhook')
  body = JSONParser().parse(request)
  logger.info(body)
  updated_at = body.get("data").get("object").get("catalog_version").get("updated_at")
  len = str(updated_at).__len__()
  update_at = '{}.00Z'.format(str(updated_at)[0:len - 5])
  logger.info(update_at)
  res = get_data(update_at)
  logger.info(res)

  return render(request, "square_up.html")




