# PUNTO DE ENTRADA DE LA APLICACIÓN
from flask_app import app

# ==========================================================
# IMPORTAR CONTROLADORES
# ==========================================================
# Aunque no utilizamos directamente la variable "tacos",
# esta importación ejecuta el módulo y registra sus rutas
# utilizando la instancia "app".
# ==========================================================

from python.cores.Inicio_sesión_registro_anabalon_annerill_09202630.secure_users.flask_app.controllers import usuarios

# EJECUTAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)
