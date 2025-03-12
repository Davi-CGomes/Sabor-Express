class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo
    self._ativo = False

  def __str__(self):
    return f'{self.titular} | {self.saldo} | {self._ativo}'
  
  @property
  def titular(self):
    return self.titular
  
  @property
  def saldo(self):
    return self.saldo
  
  @property
  def ativo(self):
    return self._ativo
  
  @classmethod
  def ativar_conta(cls, self):
    self._ativo = True

pessoa1 = ContaBancaria('Davi', 20000.00)
pessoa2 = ContaBancaria('Joao', 10000.00)

print(pessoa1)
print(pessoa2)

ContaBancaria.ativar_conta(pessoa1)

print(pessoa1)


    