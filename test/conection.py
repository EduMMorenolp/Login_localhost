import mysql.connector

# Configura los detalles de la conexión
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'usuarios'
}

# Crea una conexión a la base de datos
conn = mysql.connector.connect(**config)

# Crea un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejecuta una consulta SQL
query = "SELECT * FROM usuarios"
cursor.execute(query)

# Obtiene los resultados de la consulta
results = cursor.fetchall()

# Imprime los resultados
for row in results:
    print(row)

# Cierra el cursor y la conexión
cursor.close()
conn.close()