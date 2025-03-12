from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
  ''' Criar a classe Restaurantes e coloca os restaurantes dentro de uma lista que pode ser exibida'''
  restaurantes = []

  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria.upper()
    self._status = False

    self._cardapio = []

    self._avaliacao = []
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self._nome.ljust(20)} | {self._categoria}'

  @classmethod
  def listar_restaurantes(cls):
    #Para fazer alteração do ljust no print tem q estar entre {}
    print()
    print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | {'Status'} ')
    print('-'* 75)
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.status.ljust(25)}')
    print()

  @property
  def status(self):
    return '⌧' if self._status else '☐'
  
  def alternar_estado(self):
    self._status = not self._status

  def receber_avaliacao(self, cliente, nota):
    if 0 < nota < 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)
    
  @property
  def media_avaliacoes(self):
    '''Faz a media das avaliacoes'''
    if not self._avaliacao:
      return 'Sem avaliações'
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
    quantidade_notas = len(self._avaliacao)
    media = round(soma_das_notas/quantidade_notas, 1)
    return media

  def adicionar_no_cardapio(self, item):
    '''Ve se o item é uma instacia do cardapio e adiciona a lista cardapio'''
    if isinstance(item, ItemCardapio):
      self._cardapio.append(item)

  @property
  def exibir_cardapio(self):
    '''Enumera a lista e exibe ela'''
    print(f'Cardapio do restaurante {self._nome}\n')
    for i, item in enumerate(self._cardapio, start=1):
      if hasattr(item, 'descricao'):
        mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
        print(mensagem_prato)
      else:
        mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
        print(mensagem_bebida)

  

