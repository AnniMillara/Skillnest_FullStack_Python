from flask_app import app, bcrypt

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from flask_app.models.usuario import Usuario

@app.route("/")
@app.route("/inicio")
def inicio():
    usuario = Usuario.todos()
    
    return render_template(
        "index.html",
        usuarios = usuario
    )

@app.route("/sesion")
def sesion():
    return render_template("login.html")

@app.route("/nuevo", methods = ["POST"])
def inscribir():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    email = request.form.get("email", "").strip()
    contrasena = request.form.get("contrasena", "").strip()

    if not nombre or not apellido or not email or not contrasena:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("sesion"))

    existente = Usuario.buscar_email(email)
    if existente:
        flash("El email ya está registrado.", "danger")
        return redirect(url_for("sesion"))

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
        return redirect(url_for("sesion"))

    flash("Usuario creado correctamente.", "success")
    return redirect(url_for("perfil"))

@app.route("/entrar", methods = ["POST"])
def ingresar():
    email = request.form.get("email", "").strip()
    contrasena = request.form.get("contrasena", "").strip()

    if not email or not contrasena:
        flash("Email y contraseña son obligatorios.", "danger")
        return redirect(url_for("sesion"))

    resultado = Usuario.buscar_email(email)
    if not resultado:
        flash("Email o contraseña incorrectos.", "danger")
        return redirect(url_for("sesion"))

    if not bcrypt.check_password_hash(resultado.contrasena, contrasena):
        flash("Email o contraseña incorrectos.", "danger")
        return redirect(url_for("sesion"))

    session["usuario_id"] = resultado.id
    flash("Bienvenido de vuelta!!.", "success")
    return redirect(url_for("perfil"))

@app.route("/perfil")
def perfil():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión para ver esta página.", "danger")
        return redirect(url_for("sesion"))
    
    usuario = Usuario.buscar_id(session["usuario_id"])
    if not usuario:
        session.clear()
        flash("Usuario no encontrado.", "danger")
        return redirect(url_for("sesion"))
    
    return render_template("perfil.html", usuario=usuario)

@app.route("/cerrar")
def cerrar():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("inicio"))

@app.route("/borrar/<int:id>")
def borrar(id):
    dele = Usuario.borrar(id)
    return redirect(url_for("inicio"))