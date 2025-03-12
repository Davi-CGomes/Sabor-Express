from heranca.ex01.carro import Veiculo

class Carro(Veiculo):
  def __init__(self, marca, modelo, portas):
    super().__init__(marca, modelo)
    self.portas = portas