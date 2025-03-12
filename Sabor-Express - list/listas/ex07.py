numeros = [10, 20, 20, '0']
soma = 0 

try:
  for numero in numeros:
    soma += numero
  media = soma/len(numeros)
  print(f'{media} é a média de numeros')
except Exception as e:
  print(f'Ocorreu um erro: {e}')