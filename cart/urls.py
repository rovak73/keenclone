from django.urls import path
from .views import item_list

app_name = 'cart'

urlpatterns = [
    path('cart/', item_list, name='item-list')
]