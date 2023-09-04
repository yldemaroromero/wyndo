import requests
from django.conf import settings
from website.models import Item

def get_token(client_id, code):
  url = '{}/oauth/token?client_id={}&client_secret={}&code={}'.format(settings.CLOVER_BASE_URL, client_id, settings.CLOVER_APP_SECRET_KEY, code)
  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    return None
  
def get_data(url):
  headers = {
    'Authorization':'Bearer {}'.format(settings.CLOVER_TOKEN)
  }

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    return None
  
def create_object(data):
  res = Item.objects.create(
    itemId = data['id'],
    available = data['available'],
    name = data['name'],
    code = data.get('code', ''),
    price = data['price'],
    priceType = data['priceType'],
    defaultTaxRates = data['defaultTaxRates'],
    stockCount = data.get('stockCount', 0),
    modifiedTime = data['modifiedTime'],
    colorCode = data.get('colorCode', ''),
  )

  return res

def update_object(object, data):
  res = object.update(
    itemId = data['id'],
    available = data['available'],
    name = data['name'],
    code = data.get('code', ''),
    price = data['price'],
    priceType = data['priceType'],
    defaultTaxRates = data['defaultTaxRates'],
    stockCount = data.get('stockCount', 0),
    modifiedTime = data['modifiedTime'],
    colorCode = data.get('colorCode', ''),
  )

  return res

def delete_object(id):
  item = Item.objects.get(id=id)
  item.delete()