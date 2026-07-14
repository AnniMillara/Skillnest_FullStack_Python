from flask import Flask, render_template
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return render_template("index.html", 
            nombre= "Anubis",
            ciudad= "Santiago",
            curso= "render flask",
            anio= 2026,
            profe = False,
            tecnologias=["Python","Flask","HTML","CSS"])

@app.route("/jugador")
def jugador():
    return render_template("player.html",
                jugador= "Milkshake",
                puntaje= 9200,
                lider= False)

@app.route("/institucion")
def institucion():
    # Comentario de prueba #
    return render_template("inst.html",
                nombre= "",
                apellido= "",
                curso = "",
                institucion= "",
                anio= 2000,
                es_docente = False,
                tecnologias=["Python","Flask","HTML","CSS"])

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ Error 404 - Página no encontrada.", 404

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)