from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hi, now coming to dinner'

if __name__ == '__main__':
    app.run(debug=True)
