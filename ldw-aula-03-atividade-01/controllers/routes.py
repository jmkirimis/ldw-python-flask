import urllib.request
from flask import render_template, request, redirect, url_for
import urllib, json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/apicharacters', methods=['GET'])
    def apicharacters():
        page = request.args.get('page', 1)
        url = f'https://dragonball-api.com/api/characters?page={page}'
        res = urllib.request.urlopen(url)
        data = res.read()
        charjson = json.loads(data) 

        return render_template('apicharacters.html', charjson=charjson)