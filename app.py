from flask import Flask
from routes.tasks import tasks
from utils.db import db
from config import DATABASE_CONNECTION_URI

app = Flask (__name__)

app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI   #conexion a la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)                    #Incia la base de datos

app.register_blueprint(tasks)       #Hace referencia a las rutas que usamos
