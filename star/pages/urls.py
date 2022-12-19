from django.urls import path

from . import views

urlpatterns = [
    path('', views.RedirectPageView.as_view(), name='redirect'),
    path('', views.HomePageView.as_view(), name='home'),
]