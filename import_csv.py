import csv, time
from datetime import datetime
from app.models import create_app, db
from app.models.alumno import Alumno

app = create_app('development')

# Tamaño del lote
BATCH_SIZE = 10000

def limpiar_tabla_alumnos():
    with app.app_context():
        db.session.query(Alumno).delete()
        db.session.commit()
        print('Tabla alumnos limpiada.')

def importar_alumnos_csv(ruta_archivo):
    with app.app_context():
        with open(ruta_archivo, encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            alumnos = []
            total = 0
            for fila in reader:
                alumno = Alumno(
                    dni=fila['dni'],
                    nombre=fila['nombre'],
                    apellido=fila['apellido'],
                    email=fila['email'],
                    fecha_nacimiento=datetime.strptime(fila['fecha_nacimiento'], '%Y-%m-%d')
                )
                alumnos.append(alumno)
                # Se insertan lotes
                if len(alumnos) >= BATCH_SIZE:
                    db.session.bulk_save_objects(alumnos)
                    db.session.commit()
                    total += len(alumnos)
                    print(f"Insertados {total} alumnos...")
                    alumnos = []
            if alumnos:
                db.session.bulk_save_objects(alumnos)
                db.session.commit()
                total += len(alumnos)
            print(f'Se importaron {total} alumnos')

if __name__ == '__main__':
    limpiar_tabla_alumnos()
    start = time.time()
    importar_alumnos_csv('alumnos.csv')
    end = time.time()
    print(f"Tiempo total de importación: {end - start:.2f} segundos")