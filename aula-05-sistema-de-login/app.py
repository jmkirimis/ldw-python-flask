from flask import Flask, render_template
from controllers import routes
# Importando o model
from models.database import db
import pymysql
# Importando a biblioteca OS (comandos de S.O)
import os

# Criando instância do Flask na variável app
app = Flask(__name__, template_folder='views')  # Representa o nome do arquivo
routes.init_app(app)

# Permite ler o diretorio absoluto de um determinado arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Passando o diretório do banco ao SQLAlchemy
DB_NAME = 'thegames'
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:admin@localhost/{DB_NAME}'

# Secret para as flash messages
app.config['SECRET_KEY'] = 'thegamesscret'

#Define o tempo de duração da sessão
app.config['PERMANENT_SESSION_LIFETIME'] = 3600

# Iniciar o servidor
if __name__ == '__main__':
    #Conecta ao MySQL para criar o banco de dados (se necessário)
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Cria o banco de dados se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados está criado!")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
        
    # Inicializa a aplicação Flask e cria as tabelas no b anco
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    
    # Inicia o aplicativo Flask
    app.run(host='localhost', port=5000, debug=True)
