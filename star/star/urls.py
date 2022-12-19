from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('sauna/', include('sauna.urls')),
    path('booking/', include('booking.urls')),

]
