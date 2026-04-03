from django.urls import path

from . import views

urlpatterns = [
    path("mis-vehiculos/", views.MisVehiculosListView.as_view(), name="mis_vehiculos"),
    path("ver/<int:pk>/", views.VehiculoClienteDetailView.as_view(), name="detalle"),
    path("taller/", views.PanelTallerView.as_view(), name="panel_taller"),
    path("taller/lista/", views.VehiculoAdminListView.as_view(), name="admin_lista"),
    path("taller/nuevo/", views.VehiculoCreateView.as_view(), name="admin_crear"),
    path("taller/<int:pk>/editar/", views.VehiculoUpdateView.as_view(), name="admin_editar"),
    path("taller/<int:pk>/eliminar/", views.VehiculoDeleteView.as_view(), name="admin_eliminar"),
]
