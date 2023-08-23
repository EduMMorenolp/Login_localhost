# Sistema de Inicio de Sesión con Flask y AJAX

Este proyecto es un ejemplo simple de un sistema de inicio de sesión desarrollado utilizando el framework Flask de Python para el backend y AJAX para la interacción asíncrona con el servidor desde el frontend. El sistema permite a los usuarios ingresar su correo electrónico y contraseña para iniciar sesión, y luego muestra un mensaje de éxito o error en la misma página, sin recargarla.

## Características

- Formulario de inicio de sesión interactivo utilizando AJAX para enviar y recibir datos asincrónicamente.
- Utiliza Flask como el framework backend para manejar las solicitudes POST y verificar las credenciales.
- Se comunica con una base de datos (simulada en este ejemplo) para verificar las credenciales de inicio de sesión.
- Muestra mensajes de éxito o error en la página según la verificación de las credenciales.
- Proporciona una experiencia de usuario fluida sin necesidad de recargar la página.

## Instrucciones de Uso

1. Clone este repositorio en su máquina local.
2. Asegúrese de tener Flask instalado. Si no lo tiene, instálelo usando `pip install Flask`.
3. Cree una base de datos llamada "usuarios" en su sistema de gestión de bases de datos (por ejemplo, MySQL, PostgreSQL, SQLite, etc.).
5. Configure los detalles de conexión a la base de datos en el archivo `app.py`.
- Configura los detalles de la conexión
- <code>db_config = {'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'usuarios'}</code>
6. Ejecute la aplicación utilizando `python app.py`.
7. Abra su navegador y acceda a `http://127.0.0.1:5000`.
8. Complete el formulario de inicio de sesión con credenciales válidas o incorrectas para ver cómo se maneja la respuesta asincrónica.


**Nota**:

Este es un proyecto educativo y demostrativo diseñado para ilustrar cómo se puede crear un sistema de inicio de sesión utilizando tecnologías web modernas. La seguridad y otros aspectos críticos de un sistema real no están completamente implementados en este ejemplo.
