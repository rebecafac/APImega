# APImega
Projeto para estudar Python.

Este projeto foi criado com a finalidade de estudar Python. A idéia aqui é criar uma API que busca dados dos últimos resultados da loteria, mega sena. 🤑 🍀

Possibilita buscar as informações dos últimos concursos finalizados a partir do número ou resultado de um concurso, considerando os consursos a partir de 11/03/1996, até a data atual.
<br>

# Exemplos: 


**Endpoint**: http://127.0.0.1:5000/BuscaResultado/concurso/2400

**Resultado**:
{
    "data": {
            "_id": "618ea047cdc56eabe3ee9cbd",
            "chave": "092125263653",
            "col1": "09",
            "col2": "21",
            "col3": "25",
            "col4": "26",
            "col5": "36",
            "col6": "53",
            "concurso": "2400",
            "data": "14/08/2021",
            "premio": "",
            "qtd_ganhadores": "0"
    },
    "message": "Consulta realizada com sucesso!"
}

#  

**Endpoint**: http://127.0.0.1:5000/BuscaResultado/chave/092125263653

**Resultado**:
{
    "data": {
            "_id": "618ea047cdc56eabe3ee9cbd",
            "chave": "092125263653",
            "col1": "09",
            "col2": "21",
            "col3": "25",
            "col4": "26",
            "col5": "36",
            "col6": "53",
            "concurso": "2400",
            "data": "14/08/2021",
            "premio": "",
            "qtd_ganhadores": "0"
    },
    "message": "Consulta realizada com sucesso!"
}
  
# Projeto em desenvolvimento!
🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
<br>
<br>
Nás próximas etapas pretendo que o sistema gere números aleatórios baseados em matemática e nos últimos resultados da mega sena, más isso não garante que alguém vá ganhar algum prêmio. 😁



# Requirements
Python 3.7.X
