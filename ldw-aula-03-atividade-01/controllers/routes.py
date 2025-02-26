import urllib.request
from flask import render_template, request, redirect, url_for
import urllib, json

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/apigames', methods=['GET', 'POST'])
    def apicharacters():
        url = 'https://dattebayo-api.onrender.com/characters'
        res = urllib.request.urlopen(url)
        data = res.read()
        charjson = json.loads(data)
        
        return render_template('apicharacters.html', charjson=charjson)