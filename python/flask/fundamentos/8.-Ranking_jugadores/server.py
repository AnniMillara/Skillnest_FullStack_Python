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
    return render_template("index.html")

# Ruta para mostrar un número limitado de jugadores
@app.route("/ranking/<int: num>")
def ranking(num):
    if 1 <= num <= len(jugadores):
        jugador = next((j for j in jugadores if j["id"] <= num), None)
        return render_template("index.html", jugador = jugador)
    else:
        return abort(404)

# Ruta para personalizar el color del ranking
@app.route("/ranking")
def ranking():
    return render_template("index.html")

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True)