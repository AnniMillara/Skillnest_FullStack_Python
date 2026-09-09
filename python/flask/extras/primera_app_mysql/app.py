from flask import Flask, render_template
from mascota import Mascota
from usuario import Usuario

app = Flask(__name__)

# RUTA PRINCIPAL (mascotas)
@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)

# RUTA USUARIOS
@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)

# RUTA PARA VER UNA MASCOTA POR ID
@app.route("/mascota/<int:id>")
def ver_mascota(id):
    mascota = Mascota.get_by_id(id)
    if mascota:
        return render_template("mascota_detalle.html", mascota=mascota)
    else:
        return "Mascota no encontrada", 404

# NUEVA RUTA: buscar por nombre (actividad)
@app.route("/mascota/nombre/<string:nombre>")
def ver_mascota_por_nombre(nombre):
    mascota = Mascota.get_by_name(nombre)
    if mascota:
        return render_template("mascota_detalle.html", mascota=mascota)
    else:
        return f"No se encontró ninguna mascota con el nombre '{nombre}'", 404

# NUEVA RUTA: buscar por tipo (desafío)
@app.route("/mascotas/tipo/<string:tipo>")
def listar_mascotas_por_tipo(tipo):
    mascotas = Mascota.get_by_tipo(tipo)
    return render_template("mascotas_por_tipo.html", tipo=tipo, mascotas=mascotas)

if __name__ == "__main__":
    app.run(debug=True)