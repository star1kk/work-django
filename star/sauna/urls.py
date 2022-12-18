from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SaunaListView.as_view(), name='sauna_list'),
    path('<int:pk>/', views.SaunaDetailView.as_view(), name='sauna_detail'),
    path('new/', views.SaunaCreateView.as_view(), name='sauna_new'),
    path('<int:pk>/edit', views.SaunaUpdateView.as_view(), name='sauna_edit'),
    path('<int:pk>/delete', views.SaunaDeleteView.as_view(), name='sauna_delete')
]