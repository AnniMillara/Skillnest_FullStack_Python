from flask_app import app

# Importar los controladores para que registren sus rutas.
from flask_app.controllers import cursos, estudiantes


if __name__ == "__main__":
    app.run(debug=True)