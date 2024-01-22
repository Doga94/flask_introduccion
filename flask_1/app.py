from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return render_template("main.html", nombre_parametro=nombre)


@app.route("/edad/<int:edad>")
def m_edad(edad):
    return f'Su edad es {edad}'

#---------------------- redirects ------------------------
@app.route("/redirect")
def mi_redirec():
    return redirect(url_for('home'))

#------------------------ 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errores.html', error=error),404