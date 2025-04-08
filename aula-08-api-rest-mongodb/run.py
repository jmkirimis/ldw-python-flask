# Importando o Flask do pacote api
from api import app

# Rodando a aplicação
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)