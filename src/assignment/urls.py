
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Assignment Admin Pages"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("weather.urls")),
    path("api/", include("corn.urls")),
]
