import urllib.request
from flask import render_template, request, redirect, url_for
import urllib
import json
import locale

personagens = []
charList = []

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def init_app(app):
    @app.template_filter('format_number')
    def format_number(value):
        try:
            return locale.format_string("%d", int(value), grouping=True)
        except (ValueError, TypeError):
            return value

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/characters', methods=['GET', 'POST'])
    def characters():
        if request.method == 'POST':
            if request.form.get('personagem'):
                personagens.append(request.form.get('personagem'))
                return redirect(url_for('characters'))
        return render_template('characters.html', personagens=personagens)

    @app.route('/cadcharacter', methods=['GET', 'POST'])
    def cadcharacters():
        if request.method == 'POST':
            formdata = request.form.to_dict()
            charList.append(formdata)
            return redirect(url_for('cadcharacters'))
        return render_template('cadcharacters.html', charList=charList)

    @app.route('/apicharacters', methods=['GET', 'POST'])
    def apicharacters():
        page = request.args.get('page', 1)
        url = f'https://dragonball-api.com/api/characters?page={page}'
        res = urllib.request.urlopen(url)
        data = res.read()
        charjson = json.loads(data)

        return render_template('apicharacters.html', charjson=charjson)

    @app.route('/charinfo', methods=['GET', 'POST'])
    def charinfo():
        name = request.args.get('name')
        url = f'https://dragonball-api.com/api/characters?name={name}'
        res = urllib.request.urlopen(url)
        data = res.read()
        charinfo = json.loads(data)

        if not charinfo:
            return "Personagem não encontrado", 404

        return render_template('charinfo.html', charinfo=charinfo)
