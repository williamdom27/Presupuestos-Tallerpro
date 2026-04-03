from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import EstadoReparacion, Vehiculo


class VehicleManagerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("cliente", password="x")
        self.v = Vehiculo.objects.create(
            marca="Toyota",
            modelo="Yaris",
            patente="ABCD12",
            propietario=self.user,
            presupuesto_reparacion=350_000,
            fecha_ingreso=timezone.localdate(),
            estado_reparacion=EstadoReparacion.EN_REPARACION,
        )

    def test_del_propietario(self):
        qs = Vehiculo.objects.del_propietario(self.user)
        self.assertEqual(list(qs), [self.v])

    def test_estadisticas_taller(self):
        stats = Vehiculo.objects.estadisticas_taller()
        self.assertGreaterEqual(stats["vehiculos_activos_en_taller"], 1)
        self.assertGreaterEqual(stats["total_presupuesto_clp"], 350_000)
        self.assertTrue(any(r["codigo"] == EstadoReparacion.EN_REPARACION for r in stats["por_estado"]))
