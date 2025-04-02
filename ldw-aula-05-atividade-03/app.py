from flask import Flask, render_template
from controllers import routes
from models.database import db
import pymysql
import os

app = Flask(__name__, template_folder='views')
routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'rocketimages'
app.config['DATABASE_NAME'] = DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'
app.config['SECRET_KEY'] = 'rocketimagessecret'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 102

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
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"O banco de dados está criado!")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
        
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    
    app.run(host='localhost', port=5000, debug=True)
