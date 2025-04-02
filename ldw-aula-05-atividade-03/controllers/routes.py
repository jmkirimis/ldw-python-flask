from flask import render_template, request, redirect, url_for, flash, session
from models.database import db, Usuario, Imagem
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import Markup
import os
import uuid


def init_app(app):
    @app.before_request
    def check_auth():
        routes = ['login', 'caduser', 'home']

        if request.endpoint in routes or request.path.startswith('/static/'):
            return

        if 'user_id' not in session:
            return redirect(url_for('login'))

    @app.route('/')
    def home():
        return render_template('index.html')

    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])

    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES

    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        imagens = Imagem.query.all()
        if request.method == 'POST':
            file = request.files['file']

            if not arquivos_permitidos(file.filename):
                flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
                return redirect(request.url)

            filename = str(uuid.uuid4())
            img = Imagem(filename)
            db.session.add(img)
            db.session.commit()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso!", 'success')
            return redirect(url_for('galeria'))

        return render_template('galeria.html', imagens=imagens)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']

            user = Usuario.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.email
                nickname = user.email.split('@')
                flash(
                    f'Login bem sucedido! Bem vindo {nickname[0]}!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Falha no login. Verifique seu nome de usuário e senha.', 'danger')

        return render_template('login.html')

    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        session.clear()
        return redirect(url_for('home'))

    @app.route('/caduser', methods=['GET', 'POST'])
    def caduser():
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']

            user = Usuario.query.filter_by(email=email).first()
            if user:
                msg = Markup(
                    "Usuário já cadastrado. Faça <a href=''/login'>Login</a>")
                flash(msg, 'danger')
                return redirect(url_for('caduser'))

            else:
                hashed_password = generate_password_hash(
                    password, method='scrypt')
                new_user = Usuario(email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

                flash('Registro realizado com sucesso! Faça o login', 'success')
                return redirect(url_for('login'))

        return render_template('caduser.html')
