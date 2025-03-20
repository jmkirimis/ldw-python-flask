from flask_sqlalchemy import SQLAlchemy
# Criando uma instância do SQLAlchemy
db = SQLAlchemy()

# Classe responsável por criar a entidade "Game" no banco com seus atributos
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    ki = db.Column(db.Integer)
    kiMax = db.Column(db.String(150))
    raca = db.Column(db.String(150))
    
    # Método construtor da classe
    def __init__(self, nome, ki, kiMax, raca):
        self.nome = nome
        self.ki = ki
        self.kiMax = kiMax
        self.raca = raca
