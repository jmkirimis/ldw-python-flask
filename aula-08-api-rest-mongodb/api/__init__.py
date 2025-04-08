from flask import Flask
# Importando o Flask-Restful
from flask_restful import Api
# Importando o PyMongo
from flask_pymongo import PyMongo
# Carregando Flask
app = Flask(__name__)

# Configurando o Flask com o MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/api-movies"

# Carregando o Flask-Restful
api = Api(app)
# Carregando o PyMongo
mongo = PyMongo(app)

# Importando os recursos
from .resources import movies_resources

