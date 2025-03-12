'''Servidor rodando locamente, p rodar na internet usar um sistema de cloud'''
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
  '''
  Endpoint que exibe mensagem hello world
  '''
  return {'Hello' : 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
  '''
  Endpoint para ver os cardapios dos restaurantes
  '''
  url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
  response = requests.get(url)

  if response.status_code == 200:
    '''Verifica se a resposa da requisição foi um sucesso'''
    dados_json = response.json()
    if restaurante is None:
      return {'Dados': dados_json}

    dados_restaurante = []

    for item in dados_json:
      '''Le a lista de dados e separa por resutanrante em um dicionario, so aparece coisas de um determinado restaurante'''
      if item['Company'] == restaurante:
        dados_restaurante.append({
        'item': item['Item'],
        'price': item['price'],
        'description': item['description']
      })
    return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
  else:
    return {'Erro': f'{response.status_code} - {response.text}'}

