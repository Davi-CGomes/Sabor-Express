class Musica:
  musicas = []

  def __init__(self, nome, artista, duracao = 0):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    Musica.musicas.append(self)
  
musica1 = Musica('Under Pressure', 'Queen & David Bowie', 248)    
musica2 = Musica('Hotel California', 'Eagles', 390)