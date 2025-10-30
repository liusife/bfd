from model.livro_model import Livro
from service.livro_service import salvar_livro, listar_livros

def cadastrar_livro(isbn, titulo, usuario_cpf):
    if not isbn or not titulo or not usuario_cpf:
        return "ISBN, título e CPF do usuário são obrigatórios!"
    try:
        salvar_livro(isbn, titulo, usuario_cpf)
        return "Livro cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar livro: {str(e)}"

def obter_livros():
    return listar_livros()