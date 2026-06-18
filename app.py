from flask import Flask, render_template, request
from conexion import obtener_conexion

app = Flask(__name__)

# Página principal (GET)
@app.route("/")
def inicio():
    return render_template("form.html")


# Guardar datos (POST)
@app.route("/guardar", methods=["POST"])
def guardar():

    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    edad = request.form["edad"]
    telefono = request.form["telefono"]
    email = request.form["email"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO personas (nombres, apellidos, edad, telefono, email)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (nombres, apellidos, edad, telefono, email))

    conexion.commit()

    cursor.close()
    conexion.close()

    return "Datos guardados correctamente"


if __name__ == "__main__":
    app.run(debug=True)