class Carro:
  carros = []

  def __init__(self, modelo, cor, ano = 0):
    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    Carro.carros.append(self)

  def listar_carros():
    for carro in Carro.carros:
      print(f'{carro.modelo.ljust(20)} | {carro.cor.ljust(20)} | {carro.ano}')

carro1 = Carro('Ford ka', 'preto', 2010)
carro2 = Carro('Kwid', 'vermelho', 2015)

Carro.listar_carros()

print(Carro.carros)

    