from flask import Flask


app = Flask(__name__)


# Criando uma rota
@app.route('/')
def hello_world():
    return 'Hello, World!'


# Criando outra rota
@app.route('/about')
def about():
    return f'Página sobre o site'


# Debug para rodar o servidor local
if __name__ == '__main__':
    app.run(debug=True)


"""
PROTOCOLO HTTP
- GET -> Obter informações
- POST -> Enviar informações
- PUT -> Atualizar informações
- DELETE -> Deletar informações
- PATCH -> Atualizar parcialmente informações

NAS REQUISIÇÕES DEVOLVE AS INFORMAÇÕES NO FORMATO JSON OU XML

CÓDIGOS DE RESPOSTA HTTP
- 200 a 299 -> OK
- 300 a 399 -> Redirecionamento para outra página
- 400 a 499 -> Erro do cliente
- 500 a 599 -> Erro do servidor
- 400 -> Bad Request
- 401 -> Unauthorized
- 404 -> Not Found
- 500 -> Internal Server Error


DOCUMENTAÇÃO DE API
- Swagger -> Gratuita Swagger Editor
"""