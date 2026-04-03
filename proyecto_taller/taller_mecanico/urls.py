from django.contrib import admin
from django.urls import include, path

from vehiculos import views as v

admin.site.site_header = "Administración Taller Mecánico"
admin.site.site_title = "Taller admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.HomeView.as_view(), name="home"),
    path("cuenta/registro/", v.RegistroView.as_view(), name="register"),
    path("cuenta/", include("django.contrib.auth.urls")),
    path("vehiculos/", include(("vehiculos.urls", "vehiculos"), namespace="vehiculos")),
]
