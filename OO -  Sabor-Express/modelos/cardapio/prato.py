from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
  def __init__(self, nome, preco, descricao):
    '''Pega atributos da classe ItemCardapio'''
    super().__init__(nome, preco)
    self.descricao = descricao #Cria o atributo 
  
  def __str__(self):
    return self._nome
  
  def aplicar_desconto(self):
    self._preco -= (self._preco * 0.05)