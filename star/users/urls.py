from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path("<int:pk>/edit", views.UserUpdateView.as_view(), name='edit_user')
]