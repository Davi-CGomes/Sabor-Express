class Restaurante:
    
    def __init__(self, nome, categoria, capacidade = 0, nota_avaliacao = 0, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'


novo_restaurante = Restaurante('Santa Marmita', 'Fast Food', 200, 10)

print(novo_restaurante)