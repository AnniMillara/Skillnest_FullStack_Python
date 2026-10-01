from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_app import app
from flask_app.models.curso import Cursos
from flask_app.models.estudiante import Estudiantes


@app.route("/")
def hola():
    return redirect(url_for("cursos"))


@app.route("/cursos")
def cursos():
    cursos = Cursos.todos()
    
    return render_template(
        "cursos.html",
        cursos = cursos
    )


@app.route("/cursos/<int:id>")
def mostrar_curso(id):
    curso = Cursos.buscar_id(id)
    
    if not curso:
        flash("Por favor ingresar curso existente...", "danger")
        return redirect(url_for("cursos"))
    
    estudiantes = Estudiantes.estudiantes_por_curso(id)
    
    return render_template(
        "mostrar_curso.html",
        curso = curso,
        estudiantes = estudiantes
    )


@app.route("/cursos/crear", methods = ["POST"])
def ingresar_curso():
    nombre = request.form.get("nombre", "").strip()
    
    if not nombre:
        flash("Todos los campos son obligatorios...", "danger")
        return redirect(url_for("cursos"))
    
    validar = Cursos.buscar_nombre(nombre)
    if validar:
        flash("Este curso ya existe, por favor buscar otro nombre...", "danger")
        return redirect(url_for("cursos"))
    
    data = {
        "nombre" : nombre
    }
    
    try:
        Cursos.guardar(data)
        flash("Curso guardado correctamente!!", "success")
    except Exception as e:
        flash(f"Ups, algo salió mal: {e}", "danger")
    
    return redirect(url_for("cursos"))


@app.route("/cursos/eliminar/<int:id>")
def eliminar_curso(id):
    validar = Estudiantes.hay_estudiantes_cursos(id)
    if validar:
        flash("No se pudo eliminar el curso...", "danger")
        return redirect(url_for("cursos"))
    
    try:
        Cursos.eliminar(id)
        flash("Curso eliminado correctamente!!", "success")
    except Exception as e:
        flash(f"Ups, algo salió mal: {e}", "danger")
    
    return redirect(url_for("cursos"))