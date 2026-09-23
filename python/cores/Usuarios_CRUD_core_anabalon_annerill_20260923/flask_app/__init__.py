# INICIALIZACIÓN
from flask import Flask
app = Flask(__name__)

# SECRET KEY
app.secret_key = "clave-secreta"