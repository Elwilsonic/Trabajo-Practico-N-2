from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URI = 'postgresql+psycopg2://pprats:naranja@localhost:5432/DEV_SYSACAD'

db = SQLAlchemy()

def create_app(config_name=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app