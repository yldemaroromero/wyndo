import requests
import logging
logger = logging.getLogger('django')
from django.conf import settings

def get_token(code):
  url = '{}/oauth2/token'.format(settings.SQUARE_UP_BASE_URL)
  data = {
    "client_id": settings.SQUARE_UP_CLIENT_ID,
    "client_secret": settings.SQUARE_UP_APP_SECRET_KEY,
    "code": code,
    "grant_type": "authorization_code"
  }

  response = requests.post(url, data)

  if response.status_code == 200:
    return response.json()
  else:
    return None




