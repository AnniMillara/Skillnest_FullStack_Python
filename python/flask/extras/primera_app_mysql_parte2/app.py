from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)
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
    return render_template(
        "mascotas_por_tipo.html",
        tipo=tipo,
        mascotas=mascotas
    )


# NUEVA RUTA PARA EL DESAFÍO ESPECÍFICO
@app.route("/mascotas/perros")
def listar_perros():
    mascotas = Mascota.get_by_tipo("Perro")
    return render_template(
        "mascotas_por_tipo.html",
        tipo="Perro",
        mascotas=mascotas
    )


# ==========================================================
# CREATE - CREAR MASCOTA  ← ¡LO QUE FALTABA!
# ==========================================================
@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    """
    Recibe la información del formulario
    y crea una nueva mascota.
    """
    datos = {
        "nombre": request.form["nombre"],
        "tipo":   request.form["tipo"],
        "color":  request.form["color"]
    }
    Mascota.save(datos)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)