from django.urls import path
from .views import ProfileDetailView, ProfileListView, profile_form
from django.views.generic.edit import FormView
from . import views

# urlpatterns = [
#   path('profile/', views.profile_list, name='profiles'),
#   path('profile/', views.profile_detail, name='profile detail'),
# ]

urlpatterns = [
  path('profile/<slug:slug>/', ProfileDetailView.as_view(), name = 'profile-detail'),
  path('profile/', ProfileListView.as_view(), name = 'profile-list'),
  path('edit/', profile_form, name = 'profile-edit'),
]
