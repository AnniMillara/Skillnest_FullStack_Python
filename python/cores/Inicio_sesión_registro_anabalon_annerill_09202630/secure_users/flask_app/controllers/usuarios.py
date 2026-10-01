import re
from flask_app import app, bcrypt
from flask import render_template, request, redirect, url_for, flash, session
from flask_app.models.usuario import Usuario

@app.route("/")
@app.route("/inicio")
def inicio():
    return render_template("login.html")

@app.route("/sesion")
def sesion():
    return redirect(url_for("inicio"))

@app.route("/nuevo", methods=["POST"])
def inscribir():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip()
    contrasena = request.form.get("contrasena", "").strip()
    confirmar_contrasena = request.form.get("confirmar_contrasena", "").strip()

    if not nombre or not apellido or not email or not contrasena or not confirmar_contrasena:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("inicio"))

    if not nombre.isalpha() or len(nombre) < 2:
        flash("El nombre debe contener solo letras y al menos 2 caracteres.", "danger")
        return redirect(url_for("inicio"))

    if not apellido.isalpha() or len(apellido) < 2:
        flash("El apellido debe contener solo letras y al menos 2 caracteres.", "danger")
        return redirect(url_for("inicio"))

    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        flash("El formato del email no es válido.", "danger")
        return redirect(url_for("inicio"))

    if len(contrasena) < 8:
        flash("La contraseña debe tener al menos 8 caracteres.", "danger")
        return redirect(url_for("inicio"))

    if contrasena != confirmar_contrasena:
        flash("Las contraseñas no coinciden.", "danger")
        return redirect(url_for("inicio"))

    existente = Usuario.buscar_email(email)
    if existente:
        flash("El email ya está registrado.", "danger")
        return redirect(url_for("inicio"))

    hash_contrasena = bcrypt.generate_password_hash(contrasena).decode("utf-8")

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contrasena": hash_contrasena
    }

    resultado = Usuario.guardar(data)
    if resultado is False:
        flash("No fue posible crear el usuario.", "danger")
        return redirect(url_for("inicio"))

    session["usuario_id"] = resultado
    flash("Usuario creado correctamente.", "success")
    return redirect(url_for("perfil"))

@app.route("/entrar", methods=["POST"])
def ingresar():
    email = request.form.get("email", "").strip()
    contrasena = request.form.get("contrasena", "").strip()

    if not email or not contrasena:
        flash("Email y contraseña son obligatorios.", "danger")
        return redirect(url_for("inicio"))

    resultado = Usuario.buscar_email(email)
    if not resultado:
        flash("Email o contraseña incorrectos.", "danger")
        return redirect(url_for("inicio"))

    if not bcrypt.check_password_hash(resultado.contrasena, contrasena):
        flash("Email o contraseña incorrectos.", "danger")
        return redirect(url_for("inicio"))

    session["usuario_id"] = resultado.id
    flash("Bienvenido de vuelta!!.", "success")
    return redirect(url_for("perfil"))

@app.route("/perfil")
def perfil():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión para ver esta página.", "danger")
        return redirect(url_for("inicio"))

    usuario = Usuario.buscar_id(session["usuario_id"])
    if not usuario:
        session.clear()
        flash("Usuario no encontrado.", "danger")
        return redirect(url_for("inicio"))

    return render_template("perfil.html", usuario=usuario)

@app.route("/cerrar")
def cerrar():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("inicio"))

@app.route("/borrar/<int:id>")
def borrar(id):
    if "usuario_id" not in session or session["usuario_id"] != id:
        flash("No tienes permiso para realizar esta acción.", "danger")
        return redirect(url_for("inicio"))
    Usuario.borrar(id)
    session.clear()
    flash("Usuario eliminado correctamente.", "success")
    return redirect(url_for("inicio"))