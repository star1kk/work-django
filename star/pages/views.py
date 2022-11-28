from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'


class AddPageView(TemplateView):
    template_name = 'form.html'


def AddPageView(request):
    return render(request, "form.html")
