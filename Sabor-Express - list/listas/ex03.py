numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somar = 0

for numero in numeros:
  if numero % 2 == 1:
    somar = somar + numero
    
print(f'{somar} é a soma dos numeros impares')

