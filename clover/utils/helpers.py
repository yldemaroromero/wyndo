import logging
logger = logging.getLogger('django')
from django.conf import settings

def get_type_of_object(type):
  match type:
    case 'I':
      return 'items'
    case 'IC':
      return 'categories'
    case 'IG':
      return 'modifier groups'
    case _:
      return ''
     
def get_url(type, id):
  match type:
    case 'I':
      return '{}/{}/{}/{}'.format(settings.CLOVER_API_BASE_URL, settings.MERCHANT_ID, 'items', id)
    case 'IC':
      return '{}/{}/{}/{}'.format(settings.CLOVER_API_BASE_URL, settings.MERCHANT_ID, 'categories', id)
    case 'IG':
      return '{}/{}/{}/{}'.format(settings.CLOVER_API_BASE_URL, settings.MERCHANT_ID, 'modifier_groups', id)
    case _:
      return ''



