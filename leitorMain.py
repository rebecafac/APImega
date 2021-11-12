from flask import Flask, request
from util import Resultados as Res
import json
import os

app = Flask(__name__)
app.debug = True


# Função que realiza a requisição de post para
# gravar os últimos resultados no banco
@app.route('/Insert', methods=['POST'])
def insert_resultado():
    try:
        data = request.data
        data = data.decode('utf-8')
        if data:
            id_obj = Res().insere_resultado(
                table='resultados',
                response=json.loads(data)
            )

        print(id_obj)
        return gera_response('', len(id_obj) > 0, 200)
    except Exception as e:
        print(e)
        return gera_response(
            message='Não foi possível processar a inclusão',
            data='',
            status_code=500
        )

# Função que busca determinado resultado a partir da chave
@app.route('/BuscaResultado/<filtro>/<valor>', methods=['GET'])
def find_chave(filtro, valor):
    try:
        finds_founds = Res().find_registers(
            table='resultados',
            filtro=filtro,
            valor=valor
        )
        print(finds_founds)
        return gera_response(
            'Consulta realizada com sucesso!',
            finds_founds,
            200
        )
    except Exception as e:
        print(e)
        return gera_response(
            message='Não foi possível consultar as coordenadas!',
            data='',
            status_code=500
        )

def gera_response(message, data, status_code):
    body = {}

    if data != []:
        if message:
            body['message'] = message

        data[0]["_id"] = str(data[0]["_id"])
        body['data'] = data[0]
    else:
        body['message'] = "Registro não encontrado!"

    return body, status_code


if "__main__" == __name__:
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port, debug=True)
