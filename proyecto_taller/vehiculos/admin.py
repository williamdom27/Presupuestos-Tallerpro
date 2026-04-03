from django.contrib import admin

from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = (
        "patente",
        "marca",
        "modelo",
        "propietario",
        "presupuesto_reparacion",
        "fecha_ingreso",
        "estado_reparacion",
    )
    list_filter = ("estado_reparacion", "fecha_ingreso", "marca")
    search_fields = ("patente", "marca", "modelo", "propietario__username")
    autocomplete_fields = ("propietario",)
    date_hierarchy = "fecha_ingreso"
    ordering = ("-fecha_ingreso",)
