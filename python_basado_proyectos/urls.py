from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('apps.main.urls')),
    re_path('',include('apps.graficos.urls')),
    re_path('',include('apps.proyecto1.urls')),
    re_path('',include('apps.proyecto2.urls')),
]
