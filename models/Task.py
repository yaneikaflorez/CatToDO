from utils.db import db

class Task(db.Model):                                          # define los campos de datos que va a usar la app
    id = db.Column(db.Integer, primary_key = True)
    TaskName = db.Column(db.String(80))
    TaskDescription = db.Column(db.String(200))

    def __init__(self, TaskName, TaskDescription):        # Usamos un constructor para iniciar las variables que creamos
        self.TaskName = TaskName
        self.TaskDescription = TaskDescription

        