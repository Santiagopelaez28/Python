from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def datos():
    conn = sqlite3.connect('Stock_ropa.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos_hombre')
    datos_productos_hombre = cursor.fetchall()
    cursor.execute('SELECT * FROM productos_mujer')
    datos_productos_mujer = cursor.fetchall()
    conn.close()
    return datos_productos_hombre, datos_productos_mujer

@app.route('/')

def index():
    datos_productos_hombre, datos_productos_mujer = datos()
    return render_template('plantilla.html', datos_productos_hombre = datos_productos_hombre, datos_productos_mujer=datos_productos_mujer)

if __name__ == '__main__':
    app.run()