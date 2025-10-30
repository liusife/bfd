import streamlit as st
from controller.livro_controller import cadastrar_livro, obter_livros
from controller.usuario_controller import cadastrar_usuario, fazer_login
from dados.database import criar_tabela

# Inicialização
criar_tabela()
if 'usuario_logado' not in st.session_state:
    st.session_state.usuario_logado = None

# Área de Login/Cadastro
if not st.session_state.usuario_logado:
    st.title("📚 Biblioteca")
    tab1, tab2 = st.tabs(["Login", "Cadastro"])
    
    with tab1:
        with st.form("login_form"):
            cpf_login = st.text_input("CPF")
            submitted_login = st.form_submit_button("Entrar")
            if submitted_login:
                usuario = fazer_login(cpf_login)
                if usuario:
                    st.session_state.usuario_logado = usuario
                    st.rerun()
                else:
                    st.error("Usuário não encontrado!")

    with tab2:
        with st.form("cadastro_form"):
            cpf = st.text_input("CPF")
            nome = st.text_input("Nome")
            submitted_cadastro = st.form_submit_button("Cadastrar")
            if submitted_cadastro:
                mensagem = cadastrar_usuario(cpf, nome)
                st.success(mensagem)

else:
    # Área logada
    st.title(f"📚 Bem-vindo(a), {st.session_state.usuario_logado[1]}!")
    
    if st.button("Logout"):
        st.session_state.usuario_logado = None
        st.rerun()

    # Formulário de cadastro de livros
    st.subheader("Cadastrar Novo Livro")
    with st.form("form_livro"):
        isbn = st.text_input("ISBN")
        titulo = st.text_input("Título")
        submitted = st.form_submit_button("Cadastrar Livro")

        if submitted:
            mensagem = cadastrar_livro(isbn, titulo, st.session_state.usuario_logado[0])
            st.success(mensagem)

    # Listagem
    st.subheader("Lista de Livros Cadastrados")
    livros = obter_livros()

    if livros:
        for l in livros:
            st.write(f"**Cadastrado por:** {l[2]} | **ISBN:** {l[0]} | **Título:** {l[1]}")
    else:
        st.info("Nenhum livro cadastrado ainda.")
