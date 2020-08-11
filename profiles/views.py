from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"


class ProfileCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    success_message = "Profile was created successfully"
    success_url = reverse_lazy('profile:profile-list')

    def get_initial(self):
        initial = super(ProfileCreate, self).get_initial()
        initial.update({'email': self.request.user.email})
        return initial

    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()

        return super(ProfileCreate, self).form_valid(form)


class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    success_message = "Profile was updated successfully"
    success_url = reverse_lazy('profile:profile-list')


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-detail')

      