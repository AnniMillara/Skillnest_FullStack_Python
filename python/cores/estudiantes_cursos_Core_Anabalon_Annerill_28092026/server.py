from flask_app import app

# Importamos el controlador para registrar las rutas.
from python.cores.estudiantes_cursos_Core_Anabalon_Annerill_28092026.flask_app.controllers import usuarios


if __name__ == "__main__":
    app.run(debug=True)