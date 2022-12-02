from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add', views.AddPageView.as_view(), name='add'),
    path('sauna1', views.Sauna1PageView.as_view(), name='sauna1'),
    path('sauna2', views.Sauna2PageView.as_view(), name='sauna2'),
    path('sauna3', views.Sauna3PageView.as_view(), name='sauna3'),
]