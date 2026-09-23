# PUNTO DE ENTRADA DE LA APLICACIÓN
from flask_app import app

# IMPORTAR CONTROLADORES
from flask_app.controllers import usuarios

# EJECUTAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)
