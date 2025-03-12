x = int(input('informe a coordenada x: '))
y = int(input('informe a coordenada y: '))

if x > 0 and y > 0:
  print('primeiro quadrante')
elif x < 0 and y > 0:
  print('segundo quadrante')
elif x < 0 and y < 0:
  print('terceiro quadrante')
elif x > 0 and y < 0:
  print('quarto quadrante')
else:
  print('esta no ponto de origem')


