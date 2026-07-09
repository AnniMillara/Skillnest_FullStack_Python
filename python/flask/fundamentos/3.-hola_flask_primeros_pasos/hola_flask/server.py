from flask import Flask

app = Flask(__name__)
#  decorados de flas
#  / rama inicial
# @app.route("/") retorna la pagina inicial 
@app.route("/")
def hola_mundo():
    # lo que se retorna es ¡Hola Mundo!
    return "¡Hola Donovan!"
@app.route("/nosotros")
def nosotros():
        return "Conócenos un poco más!"
# productos
@app.route("/productos")
def productos():
        return "Conócenos los nuevos productos!"
# contactos
@app.route("/contactos")
def contactos():
        return "Ve tus nuevos contactos!"

if __name__ == "__main__":
    # es donde arranca, donde debug reinicia sin que se caiga 
    app.run(debug=True)