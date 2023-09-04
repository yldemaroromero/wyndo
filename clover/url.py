from django.urls import path

from .views import main, webhook

urlpatterns = [
  path('', main),
  path('webhook', webhook),
]
