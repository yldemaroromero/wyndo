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

def get_data(update_at):
  url = '{}/v2/catalog/search'.format(settings.SQUARE_UP_BASE_URL)
  headers = {
    'Square-Version': '2023-09-25',
    'Authorization':'Bearer {}'.format(settings.SQUARE_UP_TOKEN),
    'Content-Type': 'application/json'
  }
  data = {
   "include_deleted_objects": True,
   "include_related_objects": False,
   "begin_time": "2023-10-02T14:49:41.00Z"
  }

  print(url)
  print(headers)
  print(data)

  response = requests.post(url, headers, data)
  print(response)

  if response.status_code == 200:
    return response.json()
  else:
    return None




