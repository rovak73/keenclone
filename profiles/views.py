from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProfileFormPrv, ProfileFormPub, PhotoForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    queryset = Profile.objects.all()


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"
    queryset = Profile.objects.all()

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Profile, slug=slug_)



# class MyProfileDetailView(LoginRequiredMixin, DetailView):
#     model = get_user_model()
#     template_name = "profiles/profile_myprofile.html"



    # def get_form_kwargs(self):
    #     kwargs = super(MyProfileDetailView, self).get_initial()
    #     kwargs["user"] = self.request.user
    #     return kwargs


class ProfileCreatePub(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfileFormPub
    template_name = "profiles/profile_form.html"
    queryset = Profile.objects.all()
    success_message = "Profile was created successfully"
    success_url = reverse_lazy('profile:profile-list')

    # def form_valid(self, form):
    #     profile = form.save(commit=False)
    #     profile.user = Profile.objects.get(user=self.request.user)  # use your own profile here
    #     profile.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_initial(self):
        initial = super(ProfileCreatePub, self).get_initial()
        initial.update({'email': self.request.user.email})
        return initial

    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()

        return super(ProfileCreatePub, self).form_valid(form)


class ProfileUpdatePub(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileFormPub
    success_message = "Profile was updated successfully"
    success_url = reverse_lazy('profile:profile-list')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)

class ProfileDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = "profiles/profile_delete.html"
    success_message = "Profile was deleted successfully"
    queryset = Profile.objects.all()

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Profile, slug=slug_)

    def get_success_url(self):
        return reverse('profile:profile-list') 


def profile_picture(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        context['url'] = fs.url(name)
    return render (request, 'profiles/profile_picture.html', context)

def photo_list(request):
    photos = Profile.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'profiles/profile_picture.html', {'form': form, 'photos': photos})