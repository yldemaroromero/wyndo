from django.shortcuts import render
import logging
logger = logging.getLogger('django')
from django.conf import settings

def index(request):
  logger.info('clover')
  CLOVER_URL = "https://sandbox.dev.clover.com/oauth/authorize?client_id={}".format(settings.CLOVER_CLIENT_ID)
  SQUARE_UP_URL = "https://squareup.com/oauth2/authorize?client_id={}".format(settings.SQUARE_UP_CLIENT_ID) 
  return render(request, "index.html", {'CLOVER_URL':CLOVER_URL, 'SQUARE_UP_URL': SQUARE_UP_URL})
