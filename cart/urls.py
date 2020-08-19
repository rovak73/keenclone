from django.urls import path
from .views import ItemDetailView, ItemListView, add_to_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('cart/', ItemListView.as_view(), name='item-list'),
    path('cart/<str:slug>/', ItemDetailView.as_view(), name='item-detail'),
    path('cart/add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('cart/remove-from-cart/<slug>/',
         remove_from_cart, name='remove-from-cart'),
]
