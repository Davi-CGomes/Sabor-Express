import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
                ]

def exibir_nome(): 
  ''' Essa função exibe o nome do App '''
  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
  ''' Essa funcao exibe as opcoes do usuario '''
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Alternar estado do restaurante') 
  print('4. Sair\n')

def finalizar_app():
  ''' Essa funcao finaliza o App'''
  exibir_subtitulo('Finalizando o app')

def voltar_menu():
  ''' Essa funcao volta ao menu '''
  input('\nDigite uma tecla para voltar ao menu principal ')
  main()

def opcao_invalida():
  ''' Essa funcao é para caso a opcao escolhida seja invalida '''
  print('Opcao invalida!\n')
  voltar_menu()

def exibir_subtitulo(texto):
  ''' Essa funcao exibe o subtitulo de cada opcao '''
  os.system('cls')
  linha = '*' * (len(texto))
  print(linha)
  print(texto)
  print(linha)
  print()

def cadastrar_restaurante():
  ''' Essa função é responsavel por cadastrar um novo restaurante 

      Inputs: 
      - Nome do restaurante 
      - Categoria

      Outputs:
      - Adiciona um novo restaurante a lista de restaurantes
  '''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que será cadastrado: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
  dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado.')
  voltar_menu()

def listar_restaurante():
  ''' Essa funcao lista os restaurantes no App'''
  exibir_subtitulo('Lista dos restaurantes')

  print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
  print('-'*60)
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativado' if restaurante['ativo'] else 'desativado'

    print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

  voltar_menu()

def alternar_ativacao():
  ''' Essa funcao altera o status do restaurante '''
  exibir_subtitulo('Alternando estado do restaurante')

  nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)

  if not restaurante_encontrado:
    print('O restaurante nao foi encontrado')

  voltar_menu()


def escolher_opcao():
  ''' Essa funcao deixa o usuario escolher qual opcao ele quer'''
  try:
    opcao = int(input('Escolha uma opcao: '))
    #opcao = int(opcao)

    if opcao == 1:
      cadastrar_restaurante()
    elif opcao == 2:
      listar_restaurante()
    elif opcao == 3:
      alternar_ativacao()
    elif opcao == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  ''' Função principal '''
  os.system('cls')
  exibir_nome()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()
