from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Specialty
from django.views.generic.list import MultipleObjectMixin

# Create your views here.
class SpecialtyListView(ListView):
    model = Specialty
    template_name = "specialties/specialty_list.html"
    paginate_by = 6
    queryset = Specialty.objects.all()


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "specialties/specialty_detail.html"
    paginate_by = 6
    queryset = Specialty.objects.all()

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Specialty, slug=slug_)

