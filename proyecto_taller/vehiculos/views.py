from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import RegistroClienteForm, VehiculoForm
from .models import Vehiculo


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "Se requieren permisos de administrador del taller.")
        return super().handle_no_permission()


class HomeView(TemplateView):
    template_name = "vehiculos/home.html"


class RegistroView(CreateView):
    """Alta de usuario cliente (formulario basado en UserCreationForm)."""

    template_name = "registration/register.html"
    form_class = RegistroClienteForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Cuenta creada. Inicia sesión con tu usuario y contraseña.",
        )
        return response


class MisVehiculosListView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = "vehiculos/mis_vehiculos.html"
    context_object_name = "vehiculos"

    def get_queryset(self):
        return (
            Vehiculo.objects.del_propietario(self.request.user)
            .con_propietario_y_perfil()
        )


class VehiculoClienteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Vehiculo
    template_name = "vehiculos/detalle_cliente.html"
    context_object_name = "vehiculo"

    def test_func(self):
        v = self.get_object()
        return self.request.user.is_staff or v.propietario_id == self.request.user.id


class PanelTallerView(StaffRequiredMixin, TemplateView):
    template_name = "vehiculos/panel_taller.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["stats"] = Vehiculo.objects.estadisticas_taller()
        ctx["recientes"] = Vehiculo.objects.con_propietario_y_perfil()[:8]
        return ctx


class VehiculoAdminListView(StaffRequiredMixin, ListView):
    model = Vehiculo
    template_name = "vehiculos/admin_lista.html"
    context_object_name = "vehiculos"
    paginate_by = 15

    def get_queryset(self):
        qs = Vehiculo.objects.con_propietario_y_perfil()
        q = self.request.GET.get("q", "").strip()
        estado = self.request.GET.get("estado", "").strip()
        if q:
            qs = qs.filter(
                Q(patente__icontains=q)
                | Q(marca__icontains=q)
                | Q(modelo__icontains=q)
                | Q(propietario__username__icontains=q)
            )
        if estado:
            qs = qs.filter(estado_reparacion=estado)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        from .models import EstadoReparacion

        ctx["estados"] = EstadoReparacion.choices
        ctx["filtro_q"] = self.request.GET.get("q", "")
        ctx["filtro_estado"] = self.request.GET.get("estado", "")
        return ctx


class VehiculoCreateView(StaffRequiredMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "vehiculos/admin_form.html"
    success_url = reverse_lazy("vehiculos:admin_lista")

    def form_valid(self, form):
        messages.success(self.request, "Vehículo creado correctamente.")
        return super().form_valid(form)


class VehiculoUpdateView(StaffRequiredMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = "vehiculos/admin_form.html"
    success_url = reverse_lazy("vehiculos:admin_lista")

    def form_valid(self, form):
        messages.success(self.request, "Vehículo actualizado.")
        return super().form_valid(form)


class VehiculoDeleteView(StaffRequiredMixin, DeleteView):
    model = Vehiculo
    template_name = "vehiculos/admin_confirmar_borrar.html"
    success_url = reverse_lazy("vehiculos:admin_lista")

    def form_valid(self, form):
        messages.success(self.request, "Vehículo eliminado del sistema.")
        return super().form_valid(form)
