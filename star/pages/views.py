from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class RedirectPageView(TemplateView):
    template_name = 'redirect.html'
