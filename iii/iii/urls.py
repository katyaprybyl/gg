from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('name_/', include('name_.urls')),
    path('admin/', admin.site.urls),
]
