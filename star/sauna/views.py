from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sauna


class SaunaListView(ListView):
    model = Sauna
    template_name = 'home.html'


class SaunaDetailView(DetailView):
    model = Sauna
    template_name = 'sauna_detail.html'
    success_url = reverse_lazy('sauna_list')


class SaunaCreateView(CreateView):
    model = Sauna
    template_name = 'sauna_new.html'
    fields = ['user', 'start_time', 'end_time', 'photo1', 'photo2', 'photo3', 'description', 'full_description', 'price', 'quantity']


class SaunaUpdateView(UpdateView):
    model = Sauna
    template_name = 'sauna_edit.html'
    fields = ['user', 'start_time', 'end_time', 'photo1', 'photo2', 'photo3', 'description', 'full_description', 'price', 'quantity']


class SaunaDeleteView(DeleteView):
    model = Sauna
    template_name = 'sauna_delete.html'
    success_url = reverse_lazy('sauna_list')
