from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome':'Christopher',
        'habilidades':['C++','Python']
    },
    {
        'id':1,
        'nome':'Albert',
        'habilidades':['Java','Python']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro','mensagem':mensagem}
        return response
    def put(self, id):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            # retorna o que recebeu para confirmar a mudança
            return dados
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro','mensagem':mensagem}
            return response
    def delete(self, id):
        try:
            desenvolvedores.pop(id)
            return {'status':'sucesso','mensagem':'Registro excluído'}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro','mensagem':mensagem}
            return response

class ListaDesenvolvedores(Resource):
    def get(self):
        try:
            return desenvolvedores
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro','mensagem':mensagem}
            return response
    def post(self):
        try:
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro','mensagem':mensagem}
            return response


api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')
api.add_resource(habilidades,'/habilidades/') # interagindo com outro modulo

if __name__ == '__main__':
    app.run(debug=True)
