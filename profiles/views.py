from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.views.generic import ListView, DetailView
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"


def profile_form(request):

    user_profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=user_profile) # GET method
    if request.method == "POST":
        # Don't forget the request.POST !
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form
    }
    
    return render(request, 'profiles/profile_edit.html', context)

# class ProfileCreateView(generic_view.CreateView):
#     model = Profile
#     template_name = 'form.html'
#     form_class = ProfileForm
#     object = None

