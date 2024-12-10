from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Task import Task
from utils.db import db

tasks = Blueprint('tasks', __name__)

@tasks.route("/")                                           #la ruta principal, es decir la pagina de inicio
def home():
    tareasAgregadas = Task.query.all()                      #llamar a todos los datos guardados y almacenarlos
    return render_template('index.html', tareasAgregadas=tareasAgregadas)           #llamar al template, es decir la parte grafica
    
@tasks.route('/new', methods=['POST'])                      # esta ruta crea una nueva tarea usando el metodo POST
def add_task():
    Tarea = request.form['TaskName']                        #nombre de la tarea
    Descripcion = request.form['TaskDescription']           #descripcion de la tarea

    new_Task = Task(Tarea, Descripcion)

    db.session.add(new_Task)                                #agrega los datos a la base de datos   
    db.session.commit()                                     #finaliza la conexion con la base de datos

    flash("Tarea agregada exitosamente!")                    #mensaje para indicar el resultado de la operacion

    return redirect(url_for('tasks.home'))                  #redirecciona a la pagina principal



@tasks.route('/update/<id>', methods=['POST', 'GET'])       #esta ruta modifica una tarea creada, usando los metodos POST y GET
def update(id):
    tareaUP = Task.query.get(id)                            #obtiene la tarea a modificar segun el id

    if request.method == "POST":                            # se inicia una condicion donde si la tarea es modificada, se actualiza la base
        tareaUP.TaskName = request.form["TaskName"]                                 # de datos
        tareaUP.TaskDescription = request.form["TaskDescription"]
    
        db.session.commit()

        flash("Tarea actualizada exitosamente!")

        return redirect(url_for('tasks.home'))

    return render_template('update.html', tareaUP=tareaUP)  


@tasks.route('/delete/<id>')                                #esta ruta elimina una tarea creada
def delete(id):
    tareaDel = Task.query.get(id)
    db.session.delete(tareaDel)                             
    db.session.commit()
    
    flash("Tarea eliminada exitosamente!")   

    return redirect(url_for('tasks.home'))
