import datetime
import json
from src.modelos.modelos_dados import Sorteio
from src.banco_de_dados import DatabaseMongoDB


class Resultados:
    db = None

    def __init__(self):
        self.db = DatabaseMongoDB.connection()


    def insere_resultado(self, table, response) -> str:
        for r in response:
            id_obj = str(r['id'])
            my_obj = {"_id": id_obj}
            item = Sorteio()
            item.concurso = r['concurso']
            item.data = r['data']
            item.col1 = r['col1']
            item.col2 = r['col2']
            item.col3 = r['col3']
            item.col4 = r['col4']
            item.col5 = r['col5']
            item.col6 = r['col6']
            item.chave = r['chave']
            item.qtd_ganhadores = r['qtd_ganhadores']
            item.premio = r['premio']

            my_obj = json.loads(json.dumps(item.__dict__))

            if self.db is not None:
                self.db[table].insert_one(my_obj)

        return my_obj

    def find_registers(self, table, filtro=None, valor=None):
        objects = self.db[table]
        lists_found = []

        if filtro == 'chave':
            filter_db: object = { "chave": valor }

        elif filtro == 'data':
            filter_db: object = { "data": valor }

        elif filtro == 'concurso':
            filter_db: object = { "concurso": valor }


        for obj in objects.find(filter_db):
            lists_found.append(obj)

        return lists_found