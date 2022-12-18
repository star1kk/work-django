from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking_list'),
    path('<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('new/', views.BookingCreateView.as_view(), name='booking_new'),
    path('new/ms=<int:ms>&hc=<int:hc>', views.BookingCreateView.as_view(), name='booking_new_params'),
    path('<int:pk>/edit', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('<int:pk>/delete', views.BookingDeleteView.as_view(), name='booking_delete')
]