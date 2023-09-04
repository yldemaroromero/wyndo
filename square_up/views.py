from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from .services.square_up import get_token
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

  return render(request, "square_up.html")




