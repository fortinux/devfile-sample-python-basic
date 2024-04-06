"""
[Aplicación básica del microframework Flask de Python]

Author: Fortinux 
Date: [2024]
"""
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Mundo!"

@app.route("/servicios")
def servicios():
    return "<H1>Esta es la página de servicios</H1>"

@app.route("/contacto")
def contacto():
    return "<H1>Esta es la página de contacto</H1>"

@app.route("/admin")
def admin():
    return "<H1>Esta es la página de admin</H1>"    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')