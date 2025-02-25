from flask import render_template, request, redirect, url_for

gameList = [
    {
        'titulo': 'CS-GO',
        'ano': 2012,
        'categoria': 'FPS Online'
    }
]
        
jogadores = []

def init_app(app):
    @app.route('/')
    # View function -> função de visualização
    def home():
        return render_template('index.html')


    @app.route('/games', methods=['GET', 'POST'])
    # View function -> função de visualização
    def games():
        game = gameList[0]
        if request.method == 'POST':
           if request.form.get('jogador'):
               jogadores.append(request.form.get('jogador'))
               return redirect(url_for('games'))
            
        return render_template('games.html', game=game, jogadores=jogadores)
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            formdata = request.form.to_dict()
            gameList.append(formdata)
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html', gameList=gameList)
