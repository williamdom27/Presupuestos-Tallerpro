"""Filtros de plantilla para montos en pesos chilenos (sin decimales)."""
from django import template

register = template.Library()


@register.filter(name="clp")
def formato_clp(valor):
    if valor is None:
        return "—"
    try:
        n = int(valor)
    except (TypeError, ValueError):
        return str(valor)
    # Separador de miles típico en Chile
    texto = f"{n:,}".replace(",", ".")
    return f"${texto} CLP"
