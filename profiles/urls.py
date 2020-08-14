from django.urls import path
from .views import (
  ProfileListView,
  ProfileDetailView,
  ProfileCreatePub,
  ProfileUpdatePub,
  ProfileDeleteView,
  # MyProfileDetailView
  )
from django.views.generic.edit import FormView
from . import views

# urlpatterns = [
#   path('profile/', views.profile_list, name='profiles'),
#   path('profile/', views.profile_detail, name='profile detail'),
# ]
app_name = 'profile'

urlpatterns = [
  path('profile/', ProfileListView.as_view(), name = 'profile-list'),
  path('profile/<slug:slug>/', ProfileDetailView.as_view(), name = 'profile-detail'),
  path('profile/create/pub/', ProfileCreatePub.as_view(), name='create-pub'),
  path('profile/<slug:slug>/update/', ProfileUpdatePub.as_view(), name = 'profile-update'),
  path('profile/<slug:slug>/delete/', ProfileDeleteView.as_view(), name = 'profile-delete'),
  path('profile/usr/picture/', views.photo_list, name = 'profile-picture'),
  # path('profile/create/prv/', ProfileCreatePrv.as_view(), name='create-prv'),


  # path('profile/edit/new/', ProfileCreate.as_view(), name = 'profile-create'),
  # path('profile/<slug:slug>/update/', ProfileUpdate.as_view(), name = 'profile-update'),
  # path('accounts/update/<int:pk>/', ProfileUpdate.as_view(), name = 'profile-update'),
  # path('accounts/myaccount/<int:id>/', MyProfileDetailView.as_view(), name = 'my-profile'),
  # 
  

]
