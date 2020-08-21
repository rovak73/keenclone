from django.urls import path
from .views import (
    ItemDetailView,
    ItemListView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView
)

app_name = 'cart'

urlpatterns = [
    path('cart/', ItemListView.as_view(), name='item-list'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('cart/<str:slug>/', ItemDetailView.as_view(), name='item-detail'),
    path('cart/add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('cart/remove-from-cart/<slug>/',
         remove_from_cart, name='remove-from-cart'),
    path('cart/remove-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
