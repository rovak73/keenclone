from django.urls import path
from .views import ProfileDetailView, ProfileListView, ProfileCreate, ProfileUpdate, ProfileDelete
from django.views.generic.edit import FormView
from . import views

# urlpatterns = [
#   path('profile/', views.profile_list, name='profiles'),
#   path('profile/', views.profile_detail, name='profile detail'),
# ]
app_name = 'profile'

urlpatterns = [
  path('profile/<slug:slug>/', ProfileDetailView.as_view(), name = 'profile-detail'),
  path('profile/', ProfileListView.as_view(), name = 'profile-list'),

  path('profile/edit/new/', ProfileCreate.as_view(), name = 'profile-create'),
  path('profile/<slug:slug>/update/', ProfileUpdate.as_view(), name = 'profile-update'),
  path('profile/edit/delete/', ProfileDelete.as_view(), name = 'profile-delete'),

  path('profile/create/', ProfileCreate.as_view(), name='create'),

]
