from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return 'Hi World'

@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f'Hi {nombre}'

@app.route("/edad/<edad>")
def r_edad(edad):
    return f'you age is: {edad}'

@app.route("/templates_mostrar/<nombre>", methods = ['GET', 'POST'])
def mostrar(nombre):
    return render_template('mostrar.html', nombre=nombre)