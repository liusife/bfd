from model.usuario_model import Usuario
from service.usuario_service import salvar_usuario, autenticar_usuario

def cadastrar_usuario(cpf, nome):
    if not cpf or not nome:
        return "CPF e nome são obrigatórios!"
    
    usuario = Usuario(cpf, nome)
    try:
        salvar_usuario(usuario)
        return "Usuário cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar usuário: {str(e)}"

def fazer_login(cpf):
    if not cpf:
        return None
    return autenticar_usuario(cpf)