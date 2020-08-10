from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profile:detail')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial_base = super(ItemCreation, self).get_initial()
        initial_base['user'] = Menu.objects.get(id=1)
        return initial_base 


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-detail')

      