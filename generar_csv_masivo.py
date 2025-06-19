import csv

NUM_REGISTROS = 2_500_000
NOMBRE_ARCHIVO = 'alumnos.csv'

with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['dni', 'nombre', 'apellido', 'email', 'fecha_nacimiento'])
    for i in range(NUM_REGISTROS):
        dni = 10000000 + i
        nombre = f'Nombre{i}'
        apellido = f'Apellido{i}'
        email = f'usuario{i}@mail.com'
        fecha_nacimiento = '2000-01-01'
        writer.writerow([dni, nombre, apellido, email, fecha_nacimiento])
print(f"Archivo {NOMBRE_ARCHIVO} generado con {NUM_REGISTROS} registros.")
