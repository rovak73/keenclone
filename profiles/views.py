from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.views.generic import ListView, DetailView

class ProfileListView(ListView):
    model = Profile
    template_name = "profile_list.html"

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_detail.html"
