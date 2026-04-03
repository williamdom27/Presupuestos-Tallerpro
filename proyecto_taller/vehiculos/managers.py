"""
Consultas personalizadas y capa de acceso a datos (QuerySet / Manager).

Demuestra encapsulación de lógica de consulta en el ORM en lugar de repetir
filtros en vistas o servicios.
"""
from django.db import models
from django.db.models import Count, Sum


class VehicleQuerySet(models.QuerySet):
    """QuerySet reutilizable con métodos encadenables."""

    def del_propietario(self, user):
        return self.filter(propietario=user)

    def por_estado(self, estado: str):
        return self.filter(estado_reparacion=estado)

    def con_presupuesto_mayor_que(self, monto_clp: int):
        return self.filter(presupuesto_reparacion__gt=monto_clp)

    def ingresados_entre(self, desde, hasta):
        return self.filter(fecha_ingreso__range=(desde, hasta))

    def con_propietario_y_perfil(self):
        """Optimiza acceso al propietario (evita N+1)."""
        return self.select_related("propietario")

    def pendientes_o_en_taller(self):
        from .models import EstadoReparacion

        return self.filter(
            estado_reparacion__in=[
                EstadoReparacion.PENDIENTE,
                EstadoReparacion.EN_DIAGNOSTICO,
                EstadoReparacion.EN_REPARACION,
            ]
        )


class VehicleManager(models.Manager):
    def get_queryset(self):
        return VehicleQuerySet(self.model, using=self._db)

    def del_propietario(self, user):
        return self.get_queryset().del_propietario(user)

    def estadisticas_taller(self):
        """
        Agregación: conteo por estado y suma de presupuestos.
        Ejemplo de consulta personalizada con annotate/aggregate.
        """
        from .models import EstadoReparacion

        qs = self.get_queryset()
        labels = dict(EstadoReparacion.choices)
        raw_por_estado = (
            qs.values("estado_reparacion")
            .annotate(total=Count("id"))
            .order_by("estado_reparacion")
        )
        por_estado = [
            {
                "codigo": row["estado_reparacion"],
                "total": row["total"],
                "etiqueta": labels.get(
                    row["estado_reparacion"], row["estado_reparacion"]
                ),
            }
            for row in raw_por_estado
        ]
        total_presupuesto = qs.aggregate(suma=Sum("presupuesto_reparacion"))["suma"] or 0
        activos = qs.pendientes_o_en_taller().count()
        return {
            "por_estado": por_estado,
            "total_presupuesto_clp": total_presupuesto,
            "vehiculos_activos_en_taller": activos,
        }
