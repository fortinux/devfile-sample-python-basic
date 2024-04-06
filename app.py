"""
[Aplicación básica del microframework Flask de Python]

Author: Fortinux 
Date: [2024]
"""
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("base.html")

@app.route("/contacto")
def contacto():
    return render_template("base.html")

@app.route("/admin")
def admin():
    return render_template("base.html")    

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')