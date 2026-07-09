from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola Mundo!"

@app.route("/exito")
def exito():
    return "¡Éxito!"

@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"¡Hola {nombre}!" 

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir_presentacion(nombre, veces):
    return f"Hola {nombre}" * veces

@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"¡Chao {nombre}!"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"Hola {nombre}, tu tienes {edad} años"

if __name__ == "__main__":
    app.run(debug=True)
