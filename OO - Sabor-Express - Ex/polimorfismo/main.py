from polimorfismo.modelos.carro import Carro

carro1 = Carro('Ford', 'Focus', 'Preto')
carro2 = Carro('Chevrolet', 'Cruze', 'Prata')
carro3 = Carro('Honda', 'Civic', 'Vermelho')

print(f'Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}')
print(f'Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}')
print(f'Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}')