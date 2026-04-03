"""
Modelo de dominio del taller: vehículo y relación con el usuario propietario.

Relaciones ORM:
- Vehículo.propietario → ForeignKey a django.contrib.auth.models.User
  (muchos vehículos pueden pertenecer a un mismo usuario; cada vehículo
  tiene un único propietario asignado por el administrador).
"""
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from .managers import VehicleManager


class EstadoReparacion(models.TextChoices):
    PENDIENTE = "pendiente", "Pendiente de revisión"
    EN_DIAGNOSTICO = "diagnostico", "En diagnóstico"
    EN_REPARACION = "reparacion", "En reparación"
    ESPERA_REPUESTOS = "repuestos", "Esperando repuestos"
    LISTO = "listo", "Listo para retiro"
    ENTREGADO = "entregado", "Entregado"


class Vehiculo(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    patente = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text="Identificador único del vehículo (Chile: patente).",
    )
    propietario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="vehiculos",
        null=True,
        blank=True,
        help_text="Usuario cliente al que se asigna el vehículo.",
    )
    presupuesto_reparacion = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Monto estimado en pesos chilenos (CLP), sin decimales.",
    )
    fecha_ingreso = models.DateField()
    estado_reparacion = models.CharField(
        max_length=20,
        choices=EstadoReparacion.choices,
        default=EstadoReparacion.PENDIENTE,
        db_index=True,
    )
    notas_internas = models.TextField(blank=True)

    objects = VehicleManager()

    class Meta:
        ordering = ["-fecha_ingreso", "patente"]
        verbose_name = "vehículo"
        verbose_name_plural = "vehículos"
        indexes = [
            models.Index(fields=["estado_reparacion", "fecha_ingreso"]),
        ]

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

    def get_absolute_url(self):
        return reverse("vehiculos:detalle", kwargs={"pk": self.pk})
