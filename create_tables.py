from app.models import create_app, db
from app.models.alumno import Alumno

app = create_app()

with app.app_context():
    db.create_all()
    print('Tablas creadas correctamente en la base de datos.')
