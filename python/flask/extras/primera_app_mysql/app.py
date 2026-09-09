from flask import Flask, render_template
from mascota import Mascota
from usuario import Usuario

app = Flask(__name__)

# RUTA PRINCIPAL (mascotas)

@app.route("/")
def index():
    mascotas = Mascota.get_all()
    print(mascotas)  # para ver los objetos en consola
    return render_template("index.html", mascotas=mascotas)

# RUTA USUARIOS (EJERCICIO)

@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)

# RUTA PARA VER UNA MASCOTA POR ID (DESAFÍO)

@app.route("/mascota/<int:id>")
def ver_mascota(id):
    mascota = Mascota.get_by_id(id)
    if mascota:
        return render_template("mascota_detalle.html", mascota=mascota)
    else:
        return "Mascota no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)