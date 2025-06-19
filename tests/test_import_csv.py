import os, sys, tempfile, pytest
from app.models import create_app, db
from app.models.alumno import Alumno
from import_csv import importar_alumnos_csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        db.session.query(Alumno).delete()
        db.session.commit()
        yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

def test_importar_alumnos_csv(app):
    csv_content = 'dni,nombre,apellido,email,fecha_nacimiento\n12345678,Juan,Perez,juan@mail.com,2000-01-01\n87654321,Ana,Gomez,ana@mail.com,1999-12-31\n'
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write(csv_content)
        tmp_path = tmp.name
    try:
        importar_alumnos_csv(tmp_path)
        alumnos = Alumno.query.all()
        assert len(alumnos) == 2
        assert alumnos[0].dni == '12345678'
        assert alumnos[1].nombre == 'Ana'
    finally:
        os.remove(tmp_path)

def test_importar_alumnos_csv_volumen(app):
    num_registros = 10000
    csv_content = 'dni,nombre,apellido,email,fecha_nacimiento\n'
    for i in range(num_registros):
        csv_content += f'{10000000+i},Nombre{i},Apellido{i},email{i}@mail.com,2000-01-01\n'
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as tmp:
        tmp.write(csv_content)
        tmp_path = tmp.name
    try:
        importar_alumnos_csv(tmp_path)
        alumnos = Alumno.query.all()
        assert len(alumnos) == num_registros
    finally:
        os.remove(tmp_path)
