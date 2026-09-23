# CONTROLADOR DE USUARIOS
from flask_app.models.usuario import Usuario
from flask_app import app
from flask import (
    render_template,
    redirect,
    request,
    url_for
)

# Listar usuarios
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template(
        "index.html",
        usuarios=todos_los_usuarios
    )

# Mostrar un formulario
@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("nuevo.html")

# Crear un formulario
@app.route("/usuarios/crear", methods=["POST"])
def crear():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(datos)
    return redirect(
        url_for("usuarios")
    )

# Ver detalle
@app.route("/usuarios/<int:id>")
def detalle(id):
    datos = {
        "id": id
    }
    usuario = Usuario.get_one(datos)

    if usuario is None:
        return (
            "Usuario no encontrado",
            404
        )

    return render_template(
        "detalle.html",
        usuario=usuario
    )

# Mostrar formulario
@app.route("/usuarios/editar/<int:id>")
def editar(id):
    datos = {
        "id": id
    }
    usuario = Usuario.get_one(datos)

    if usuario is None:
        return (
            "Usuario no encontrado",
            404
        )

    return render_template(
        "editar.html",
        usuario=usuario
    )

# Procesar edición
@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar(id):
    datos = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.update(datos)
    return redirect(
        url_for(
            "detalle",
            id=id
        )
    )

# Eliminar usuario
@app.route("/usuarios/borrar/<int:id>")
def borrar(id):
    datos = {
        "id": id
    }
    Usuario.delete(datos)
    return redirect(
        url_for("usuarios")
    )