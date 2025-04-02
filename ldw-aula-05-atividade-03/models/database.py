from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(200))

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, filename):
        self.filename = filename
