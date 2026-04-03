from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import EstadoReparacion, Vehiculo


class RegistroClienteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "styled-input")


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            "marca",
            "modelo",
            "patente",
            "propietario",
            "presupuesto_reparacion",
            "fecha_ingreso",
            "estado_reparacion",
            "notas_internas",
        ]
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type": "date"}),
            "notas_internas": forms.Textarea(attrs={"rows": 3}),
            "estado_reparacion": forms.Select(choices=EstadoReparacion.choices),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "styled-input")

    def clean_patente(self):
        p = self.cleaned_data["patente"].strip().upper()
        return p
