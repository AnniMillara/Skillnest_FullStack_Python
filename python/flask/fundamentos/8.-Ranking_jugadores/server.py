from flask import Flask, render_template, abort

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
    {"nombre": "AlexGamer", "puntaje": 5000},
    {"nombre": "PixelMaster", "puntaje": 7500},
    {"nombre": "ShadowNinja", "puntaje": 8200},
    {"nombre": "CyberWarrior", "puntaje": 9100},
    {"nombre": "UltraNoob", "puntaje": 3000}
]


# Ruta para mostrar el ranking de jugadores
@app.route("/ranking")
def ranking():
    return render_template(
        "index.html",
        jugadores=jugadores,
        color=None
    )
# Ruta para mostrar un número limitado de jugadores
@app.route("/ranking/<int:cantidad>")
def ranking_limitado(cantidad):
    if 1 <= cantidad <= 5:
        return render_template("index.html",
                                jugadores=jugadores[:cantidad],
                                color=None)
    else:
        return abort(404)

# Ruta para personalizar el color del ranking
@app.route("/ranking/<int:cantidad>/<color>")
def ranking_color(cantidad, color):
    return render_template("index.html",
                        jugadores=jugadores[:cantidad],
                        color=color
                        )

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)