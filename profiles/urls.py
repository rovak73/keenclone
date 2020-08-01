from django.urls import path
from .views import ProfileDetailView, ProfileListView



# urlpatterns = [
#   path('profile/', views.profile_list, name='profiles'),
#   path('profile/', views.profile_detail, name='profile detail'),
# ]

urlpatterns = [
  path('<slug:slug>', ProfileDetailView.as_view(), name = 'profile_detail'),
  path('', ProfileListView.as_view(), name = 'profile_list'),
]
