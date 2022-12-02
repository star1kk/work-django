from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'


class AddPageView(TemplateView):
    template_name = 'form.html'


class Sauna1PageView(TemplateView):
    template_name = 'saunaPage/sauna1.html'


class Sauna2PageView(TemplateView):
    template_name = 'saunaPage/sauna2.html'


class Sauna3PageView(TemplateView):
    template_name = 'saunaPage/sauna3.html'
