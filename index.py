from app import app  
from utils.db import db

with app.app_context():               # crea los campos que vamos a usar en la base de datos apenas se
    db.create_all()                   # ejecute la aplicacion por primera vez

if __name__ == "__main__":            # inicia la aplicacion
    app.run(debug=True)            

