from django.urls import path
from .views import SpecialtyListView, SpecialtyDetailView


app_name = 'specialty'

urlpatterns = [
  path('specialty/', SpecialtyListView.as_view(), name = 'specialty-list'),
  path('specialty/<slug:slug>/', SpecialtyDetailView.as_view(), name = 'specialty-detail')
]