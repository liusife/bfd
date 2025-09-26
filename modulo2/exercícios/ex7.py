class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo, autor):
        self.livros.append({'titulo': titulo, 'autor': autor})

    def exibir_livros(self):
        for livro in self.livros:
            print(f"Título: {livro['titulo']} \nAutor: {livro['autor']}\n")

# Exemplo de uso:
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis")
biblioteca.adicionar_livro("O Alquimista", "Paulo Coelho")
biblioteca.exibir_livros()