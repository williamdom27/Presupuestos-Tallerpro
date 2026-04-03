# Sistema de Gestión de Reparaciones de Vehículos

Aplicación web desarrollada con Django para la gestión de vehículos en un taller mecánico.
El sistema permite registrar vehículos, visualizar su estado de reparación y administrarlos mediante una interfaz web y el panel de administración de Django.

---

## Descripción del proyecto

Este proyecto implementa un sistema básico de gestión para talleres mecánicos utilizando el framework Django.
La aplicación permite almacenar información de vehículos, consultar su estado de reparación y administrarlos mediante herramientas integradas del framework.

El desarrollo incluye el uso del ORM de Django, migraciones de base de datos, consultas personalizadas y el uso de aplicaciones preinstaladas del framework.

---

## Tecnologías utilizadas

* Python 3
* Django
* SQLite
* HTML
* CSS

---

## Estructura del proyecto

```
proyecto_taller/
│
├── vehiculos/            # Aplicación principal del sistema
├── taller_mecanico/      # Configuración del proyecto Django
├── templates/            # Plantillas HTML
├── static/               # Archivos estáticos
├── venv/                 # Entorno virtual
├── db.sqlite3            # Base de datos SQLite
└── manage.py             # Script principal de administración
```

---

## Instalación del proyecto

### 1. Clonar o descargar el repositorio

```
git clone <url-del-repositorio>
```

O descargar el archivo ZIP y extraerlo en el equipo.

---

### 2. Crear el entorno virtual

Desde la carpeta del proyecto ejecutar:

```
python -m venv venv
```

---

### 3. Activar el entorno virtual

En Windows:

```
venv\Scripts\activate
```

En Linux o Mac:

```
source venv/bin/activate
```

---

### 4. Instalar dependencias

```
pip install django
```

---

## Migraciones de la base de datos

Para crear las tablas necesarias ejecutar:

```
python manage.py makemigrations
python manage.py migrate
```

---

## Crear un superusuario

Para acceder al panel de administración de Django:

```
python manage.py createsuperuser
```

Se solicitarán los siguientes datos:

* nombre de usuario
* correo electrónico
* contraseña

---

## Ejecución del servidor

Para iniciar el servidor de desarrollo ejecutar:

```
python manage.py runserver
```

La aplicación estará disponible en:

```
http://127.0.0.1:8000
```

---

## Uso de la aplicación

### Página principal

La página principal muestra la lista de vehículos registrados en el sistema.
Desde esta vista se puede visualizar información relevante como:

* Marca del vehículo
* Modelo
* Año
* Estado de reparación

---

### Panel de administración

Django incluye un panel de administración integrado para gestionar los datos del sistema.

Acceso:

```
http://127.0.0.1:8000/admin
```

Desde el panel se pueden realizar las siguientes acciones:

* Crear vehículos
* Editar vehículos
* Eliminar vehículos
* Administrar usuarios del sistema

---

## Consultas a la base de datos

Ejemplo de consulta SQL utilizada para visualizar todos los vehículos registrados:

```
SELECT * FROM vehiculos_vehiculo;
```

Consulta para obtener únicamente los vehículos en proceso de reparación:

```
SELECT * FROM vehiculos_vehiculo
WHERE estado_reparacion='en_proceso';
```

Estas consultas permiten verificar el correcto almacenamiento de los datos en la base de datos.

---

## Funcionalidades CRUD

El sistema implementa las operaciones básicas de gestión de datos:

| Operación | Descripción                              |
| --------- | ---------------------------------------- |
| Create    | Registro de nuevos vehículos             |
| Read      | Visualización de vehículos registrados   |
| Update    | Modificación de información de vehículos |
| Delete    | Eliminación de registros                 |

---

## Aplicaciones preinstaladas de Django utilizadas

El proyecto utiliza varias aplicaciones incluidas en Django que facilitan el desarrollo:

* django.contrib.admin
* django.contrib.auth
* django.contrib.sessions
* django.contrib.messages

Estas aplicaciones permiten gestionar usuarios, autenticación y administración general del sistema.

---

## Posibles mejoras futuras

Algunas mejoras que podrían implementarse en versiones futuras del sistema:

* Registro de clientes del taller
* Historial de reparaciones por vehículo
* Sistema de facturación
* Dashboard con estadísticas
* API REST utilizando Django REST Framework

---

## Autor

Proyecto desarrollado como parte de un módulo académico de desarrollo backend con Django.
