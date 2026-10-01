from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_app import app
from flask_app.models.estudiante import Estudiantes
from flask_app.models.curso import Cursos


@app.route("/estudiantes/nuevo")
def nuevo_estudiante():
    cursos = Cursos.todos()
    
    return render_template(
        "nuevo_estudiante.html",
        cursos = cursos
    )


@app.route("/estudiantes/crear", methods = ["POST"])
def ingresar_estudiante():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad = request.form.get("edad", "").strip()
    curso_id = request.form.get("curso_id", "").strip()
    
    if not nombre or not apellido or not edad or not curso_id:
        flash("Todos los campos son obligatorios...", "danger")
        return redirect(url_for("nuevo_estudiante"))
    
    try:
        edad = int(edad)
        curso_id = int(curso_id)
    except ValueError:
        flash("Ha ocurrido un error :(...", "danger")
        return redirect(url_for("nuevo_estudiante"))
    
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "curso_id": curso_id
    }
    
    try:
        Estudiantes.guardar(data)
        flash("Estudiante guardado correctamente!!", "success")
    except Exception as e:
        flash(f"Ups, algo salió mal: {e}", "danger")
    
    return redirect(url_for("cursos"))

@app.route("/estudiantes/editar/<int:id>")
def editar_estudiante(id):
    estudiante = Estudiantes.buscar_id(id)
    
    if not estudiante:
        flash("El estudiante no existe.", "danger")
        return redirect(url_for("cursos"))
    
    cursos = Cursos.todos()
    
    return render_template(
        "editar_estudiante.html",
        estudiante = estudiante,
        cursos = cursos
    )

@app.route("/estudiantes/modificar/<int:id>", methods = ["POST"])
def actualizar_estudiante(id):
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad = request.form.get("edad", "").strip()
    curso_id = request.form.get("curso_id", "").strip()

    if not nombre or not apellido or not edad or not curso_id:
        flash("Todos los campos son obligatorios...", "danger")
        return redirect(url_for("editar_estudiante", id = id))

    try:
        edad = int(edad)
        curso_id = int(curso_id)
    except ValueError:
        flash("Ha ocurrido un error...", "danger")
        return redirect(url_for("editar_estudiante", id = id))

    data = {
        "id_estudiante": id,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "curso_id": curso_id
    }

    try:
        Estudiantes.editar(data)
        flash("Estudiante actualizado correctamente!!", "success")
    except Exception as e:
        flash(f"Ups, algo salió mal: {e}", "danger")

    return redirect(url_for("cursos"))


@app.route("/estudiantes/eliminar/<int:id>")
def eliminar_estudiante(id):
    try:
        Estudiantes.eliminar(id)
        flash("Estudiante eliminado correctamente!!", "success")
    except Exception as e:
        flash(f"Ups, algo salió mal: {e}", "danger")
    
    return redirect(url_for("cursos"))