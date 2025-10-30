from model.livro_model import Livro
from service.livro_service import salvar_livro, listar_livros

def cadastrar_livro(isbn: str, titulo: str, usuario_cpf: str):
    if not isbn or not titulo or not usuario_cpf:
        return "Preencha todos os campos!"
    livro = Livro(isbn, titulo, usuario_cpf)
    try:
        salvar_livro(livro)
        return f"Livro '{titulo}' cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar livro: {e}"
    
def obter_livros():
    return listar_livros()