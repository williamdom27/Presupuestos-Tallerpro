"""
Configuración del proyecto Taller Mecánico.

Incluye apps preinstaladas de Django (admin, auth, sessions, etc.) y ajustes
regionales para Chile (CLP, zona horaria Santiago).
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-dev-cambiar-en-produccion"

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# --- Aplicaciones instaladas (lección: apps preinstaladas de Django) ---
# django.contrib.admin: panel de administración
# django.contrib.auth: usuarios, grupos, permisos (User, Group, Permission)
# django.contrib.contenttypes: framework de tipos de contenido (GenericForeignKey)
# django.contrib.sessions: sesiones HTTP (cookie sessionid)
# django.contrib.messages: mensajes flash (framework de mensajes)
# django.contrib.staticfiles: servicio y recolección de archivos estáticos
# django.contrib.humanize: filtros de plantilla (intcomma para miles en CLP)
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "vehiculos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "taller_mecanico.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "taller_mecanico.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "vehiculos:mis_vehiculos"
LOGOUT_REDIRECT_URL = "home"
