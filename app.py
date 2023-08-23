from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

app = Flask(__name__)

# Configura los detalles de la conexión
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'usuarios'
}

# Función para establecer una conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar_cuenta():
    nombre = request.form['nombre']
    correo = request.form['email']
    contrasena = request.form['contrasena']

    contrasena_hash = generate_password_hash(contrasena)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"
        values = (nombre, correo, contrasena_hash)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return """
                <h1>Cuenta creada exitosamente</h1>
                <form action="/" method="get">
                    <button type="submit">Volver a la página de inicio</button>
                </form>
            """
    except Exception as e:
        return f"Error al registrar la cuenta: {str(e)}"

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    correo = request.form['emailInicioSesion']
    contrasena = request.form['contrasenaSesion']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT contrasena FROM usuarios WHERE correo = %s"
        cursor.execute(query, (correo,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result and check_password_hash(result[0], contrasena):
            return """
                <h1>Inicio de sesión exitoso</h1>
                <form action="/" method="get">
                    <button type="submit">Volver a la página de inicio</button>
                </form>
            """
        else:
            return """
                <h1>Credenciales incorrectas</h1>
                <form action="/" method="get">
                    <button type="submit">Volver a la página de inicio</button>
                </form>
            """
    except Exception as e:
        return f"Error al iniciar sesión: {str(e)}"
    
@app.route('/cuentas', methods=['GET'])
def mostrar_cuentas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT nombre, correo FROM usuarios"
        cursor.execute(query)
        cuentas = cursor.fetchall()

        cursor.close()
        conn.close()

        # Devuelve los datos en formato JSON
        return jsonify(cuentas=cuentas)
    except Exception as e:
        return f"Error al obtener las cuentas: {str(e)}"
    
    
if __name__ == '__main__':
    app.run(debug=True)

