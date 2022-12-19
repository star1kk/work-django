from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class RedirectPageView(TemplateView):
    template_name = 'redirect.html'


class AddPageView(TemplateView):
    template_name = 'form.html'


class SaunaOnePageView(TemplateView):
    template_name = 'saunaPage/sauna1.html'


class SaunaTwoPageView(TemplateView):
    template_name = 'saunaPage/sauna2.html'


class SaunaThreePageView(TemplateView):
    template_name = 'saunaPage/sauna3.html'
