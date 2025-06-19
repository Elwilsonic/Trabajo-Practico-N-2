# Trabajo Práctico N°2 - Importación Masiva de Alumnos
INTEGRANTES:
- Arreceygor Lucas
- Batista Martina
- Cabeza Florencia
- Cardozo Leandro
- Peñalbe Hernan

Este proyecto importa millones de registros de alumnos desde un archivo CSV a la base de datos `DEV_SYSACAD` usando Python, Flask, SQLAlchemy y PostgreSQL.

## Estructura del proyecto

```
TPN°2/
├── app/
│   ├── __init__.py
│   ├── alumno.py
├── import_csv.py
├── create_tables.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_import_csv.py
```

## Requisitos
- Python 3.8+
- PostgreSQL
- Flask
- Flask-SQLAlchemy
- psycopg2-binary

## Instalación
1. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
2. Crea la base de datos y el usuario en PostgreSQL:
   ```sql
   CREATE USER tu_usuario WITH PASSWORD 'tu_contraseña';
   CREATE DATABASE "DEV_SYSACAD" OWNER tu_usuario;
   GRANT ALL PRIVILEGES ON DATABASE "DEV_SYSACAD" TO tu_usuario;
   ```
3. Configura la URI de conexión en `app/__init__.py`:
   ```python
   DB_URI = 'postgresql+psycopg2://tu_usuario:tu_contraseña@localhost:5432/DEV_SYSACAD'
   ```

## Uso
1. Crea las tablas en la base de datos:
   ```sh
   python create_tables.py
   ```
2. Importa los alumnos desde un archivo CSV:
   ```sh
   python import_csv.py
   ```
   (Asegúrate de tener el archivo `alumnos.csv` en la raíz del proyecto o ajusta la ruta en el script.)

## Pruebas
Para ejecutar los tests automáticos:
```sh
python -m pytest tests
```