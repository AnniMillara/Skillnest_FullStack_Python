from flask import Flask, render_template
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route('/bienvenido')
def bienvenido():
#Enviamos 2 nuevos argumentos
    return render_template('index.html', cancion="dale a tu cuerpo alegría macarena", repite=5)
# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)