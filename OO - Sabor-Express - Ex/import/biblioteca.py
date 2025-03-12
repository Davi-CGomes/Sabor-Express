from ex01 import Livro

livro_novo = Livro('teste', 'eu', 2025)

print(f'livro antes de emprestar: {livro_novo.disponivel}')
livro_novo.emprestar()
print(f'livro depois de emprestar: {livro_novo.disponivel}')

ano_especifico = 2025
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")