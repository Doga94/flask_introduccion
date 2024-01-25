from flask import Flask, render_template

app = Flask(__name__)

base_usuario = "David"
base_contra = "David123"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login/<string:usuario>/<string:passw>")
def login(usuario, passw):
    if usuario == base_usuario and passw == base_contra:
        return "Bienvenid@"
    else:
        return "Usuario o contraseña errados"

@app.route("/suma/<int:num_1>/<int:num_2>")
def suma(num_1, num_2):
    return f"El resultado de {num_1} y {num_2} es: <h1>{num_1+num_2}</h1>"