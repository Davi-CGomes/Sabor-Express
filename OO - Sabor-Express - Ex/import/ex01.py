class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.disponivel = True
  
  def __str__(self):
    return (f'{self.titulo} | {self.autor} | {self.ano_publicacao} | {self.disponivel}')
  
  def emprestar(self):
    self.disponivel = False

  @staticmethod
  def verificar_disponibilidade(ano):
    livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]

livro1 = Livro('Aprendendo Python', 'John Doe', 2022)
livro2 = Livro('Data Science Fudamentals', 'Jane Smith', 2020)
livro3 = Livro('Python Cookbook', 'Samuel Developer', 2019)

Livro.livros = [livro1, livro2, livro3]

print(f"Antes de emprestar: Livro 3 disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro 3 disponível? {livro3.disponivel}")

print(livro1)
print(livro2)