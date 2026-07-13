from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def ingreso():
    return '𑄝੭'

# Ruta genérica para explorar enrutamiento
@app.route("/mas")
def conocer():
    return '≽^• ˕ • ྀི≼ ¿Qué ruta estás buscando? ¡Prueba con diferentes direcciones!'

# Rutas dinámicas para personalización
@app.route('/yo/<nombre>')
def persona(nombre):
    return f'ּ֯ . ❥ ּ֯ ┆꒰ {nombre} .ᐟ ꒱'

# Ruta que repite un mensaje varias veces
@app.route('/mensaje/<pal>/<int:cant>')
def mensj(pal, cant):
    return f'{pal} ' * cant

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)