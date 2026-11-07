Sistema de Reporte de Fallas de Computadoras de Laboratorio

Proyecto Integrador – Tarea 10

Descripción del proyecto

El Sistema de Reporte de Fallas de Computadoras de Laboratorio es una aplicación web desarrollada para facilitar el registro, consulta y seguimiento de las fallas que presentan los equipos informáticos dentro de los laboratorios.

El sistema permite registrar nuevos reportes, consultar la información de las fallas y actualizar su estado cuando se registra una solución.

Tecnologías utilizadas

- Python
- Flask
- MySQL
- XAMPP
- Visual Studio Code
- mysql-connector-python
- python-dotenv

Funcionalidades principales

- Registrar fallas: permite ingresar nuevos reportes indicando el equipo, la categoría y la descripción del problema.
- Consultar reportes: permite visualizar los reportes registrados y acceder a sus detalles.
- Registrar soluciones: permite agregar la solución aplicada a una falla.
- Actualizar estados: permite cambiar el estado de un reporte a «Resuelto».
- Almacenar información: guarda los reportes en una base de datos MySQL.

Arquitectura del proyecto

El sistema utiliza una arquitectura de tres capas para organizar el código y separar sus responsabilidades.

src/
│
├── business/
│   ├── __init__.py
│   └── logica.py
│
├── data/
│   ├── __init__.py
│   ├── almacenamiento.py
│   └── conexion.py
│
├── presentation/
│   ├── __init__.py
│   └── app.py
│
└── probar_conexion.py

Capa de presentación: contiene la aplicación Flask y la interfaz con la que interactúa el usuario.

Capa de lógica de negocio: procesa las operaciones y reglas relacionadas con los reportes.

Capa de acceso a datos: administra la conexión con MySQL y las operaciones de almacenamiento, consulta y actualización.

Base de datos

El proyecto utiliza una base de datos MySQL llamada "reporte_fallas", organizada en las siguientes tablas:

- "laboratorios": almacena la información de los laboratorios.
- "equipos": almacena los equipos registrados y su relación con los laboratorios.
- "reportes": almacena los reportes de fallas, sus estados y soluciones.

Instalación y configuración

1. Instalar las dependencias

Desde la carpeta principal del proyecto, ejecutar:

pip install -r requirements.txt

2. Configurar MySQL

Iniciar el servicio MySQL desde XAMPP y crear la base de datos:

CREATE DATABASE reporte_fallas;

Crear las tablas "laboratorios", "equipos" y "reportes" utilizando el script SQL del proyecto.

3. Configurar las variables de entorno

Crear un archivo ".env" en la carpeta principal del proyecto con la siguiente estructura:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=reporte_fallas
FLASK_SECRET_KEY=colocar_una_clave_privada

Completar los valores de acuerdo con la configuración local de MySQL.

Importante: el archivo ".env" no debe subirse al repositorio, ya que contiene información privada de configuración.

4. Ejecutar la aplicación

Abrir una terminal dentro de la carpeta "src" y ejecutar:

python -m presentation.app

Luego abrir el navegador e ingresar a:

http://127.0.0.1:5000

Pruebas realizadas

Se realizaron pruebas para comprobar las principales operaciones del sistema:

- Conexión exitosa entre Python y MySQL.
- Registro de nuevos reportes.
- Consulta de reportes almacenados.
- Visualización de los detalles de cada reporte.
- Registro de soluciones.
- Actualización del estado de los reportes.

Objetivo del proyecto

Facilitar la administración y el seguimiento de las fallas de los equipos informáticos de los laboratorios, mediante una aplicación web conectada a una base de datos que permita mantener la información organizada y accesible.

---

Proyecto Integrador – Tarea 10

Ingeniería en Sistemas
