from django.urls import path

from . import views

urlpatterns = [
    path('', views.RedirectPageView.as_view(), name='redirect'),
    path('', views.HomePageView.as_view(), name='home'),
    path('add', views.AddPageView.as_view(), name='add'),
    path('saunaOne', views.SaunaOnePageView.as_view(), name='saunaOne'),
    path('saunaTwo', views.SaunaTwoPageView.as_view(), name='saunaTwo'),
    path('saunaThree', views.SaunaThreePageView.as_view(), name='saunaThree'),
]