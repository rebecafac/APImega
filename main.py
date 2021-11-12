import fitz
import json
import requests
from flask import Flask, request
from util import Resultados as Res
import os


app = Flask(__name__)
app.debug = True


# Função que realiza a requisição de post para
# gravar os últimos resultados no banco
@app.route('/Insert', methods=['POST'])
def insert_resultado():
    # main()
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


def gera_response(message, data, status_code):
    body = {}

    if message:
        body['message'] = message

    body['data'] = data

    return body, status_code

def main():
    conteudo = ""

    with fitz.open("Arquivo.pdf") as pdf:
        for pagina in pdf:
            conteudo += pagina.getText()

    obJson = {}
    concursos = []
    index = 2423
    dados = ""
    inicio = 0
    fim = 47
    isNotCabec = False
    concurso = ""
    data = ""
    col1 = ""
    col2 = ""
    col3 = ""
    col4 = ""
    col5 = ""
    col6 = ""
    chave = ""
    qtd_ganhadores = ""
    premio = ""

    # Captura linha a linha do pdf
    for x in range(5607):

        if x == 0:
            inicio = 0
            fim = 47

        else:
            dados = conteudo[fim + 1:]
            inicio = fim + 1
            fim = dados.find("\n") + inicio

        linha = conteudo[inicio: fim]

        isNotCabec = linha.find('Data') == -1 and linha.find('Gan.') == -1 and linha.find(
            'Todos os resultados da Mega Sena - Rede Loteria') == -1

        # Avalia qual tipo de informação a linha possui se não for linha de cabeçalho
        if isNotCabec:

            # Número do concurso
            if len(linha) <= 4:
                concurso = linha

            # Data e chave
            elif len(linha) > 23:
                data = linha[0:10]
                col1 = linha[11:13]
                col2 = linha[14:16]
                col3 = linha[17:19]
                col4 = linha[20:22]
                col5 = linha[23:25]
                col6 = linha[26:28]
                chave = col1 + col2 + col3 + col4 + col5 + col6
                qtd_ganhadores = linha[29:30]

            # Valor do prêmio
            elif linha.find(",") > -1:
                premio = linha

            if concurso != '' and data != '' and chave != '':
                index = index - 1
                concursos.append({"id": index,
                                  "concurso": concurso,
                                  "data": data,
                                  "col1": col1,
                                  "col2": col2,
                                  "col3": col3,
                                  "col4": col4,
                                  "col5": col5,
                                  "col6": col6,
                                  "chave": chave,
                                  "qtd_ganhadores": qtd_ganhadores,
                                  "premio": premio
                                  }
                                 )

                concurso = ""
                data = ""
                col1 = ""
                col2 = ""
                col3 = ""
                col4 = ""
                col5 = ""
                col6 = ""
                chave = ""
                qtd_ganhadores = ""
                premio = ""


    print(concursos)

if "__main__" == __name__:
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port, debug=True)




