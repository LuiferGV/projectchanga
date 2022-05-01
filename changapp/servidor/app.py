
from curses import flash
from flask import Flask , render_template, url_for ,request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#from requests import request

# congifuracion de la base de datos y de flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'
db  = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content =db.Column(db.String(200))
    done = db.Column(db.Boolean)
#configuracion inicio y datos para la base de datos
@app.route("/")
def inicio():
    tasks  = Task.query.all()
    return render_template("ini.html", tasks  = tasks) # tasks agrupa todas las tareas y muestra 
# corecion del formulario html a la base de datos 
@app.route('/create-task', methods=['POST']) # metodo post es el metodo de conexion y create task es la ruta 
def create(): # task es el nombre en el que guardamos la tarea
    task = Task(content=request.form['content'], done = False)
    db.session.add(task)
    db.session.commit()
    return redirect (url_for('inicio'))


#eliminar datos 
@app.route("/delete/<id>")
def delete(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect (url_for('inicio'))


if __name__ == "__main__":
    app.run(debug=True)