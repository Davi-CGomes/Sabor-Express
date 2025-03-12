class Restaurante:
  nome = ''
  categoria = ''
  status = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.status = True

if restaurante_pizza.categoria == 'Fast Food':
  print('A categoria é Fast Food.')
else:
  print('A categoria não é Fast Food.')

if restaurante_praca.status:
  print("O restaurante está ativo.")
else:
  print("O restaurante está inativo.")

print(vars(restaurante_praca))

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}, Status: {restaurante_praca.status}')