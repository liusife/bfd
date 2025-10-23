import streamlit as st
from controller.livro_controller import cadastrar_livro, obter_livros
from dados.database import criar_tabela

# Criar tabela na inicialização
criar_tabela()

st.title("📚 Cadastro de Livros")

#formulário
st.subheader("Cadastrar Novo Livro")
with st.form("form_livro"):
    isbn = st.text_input("ISBN")
    titulo = st.text_input("Título")
    submitted = st.form_submit_button("Cadastrar Livro")

    if submitted:
        mensagem = cadastrar_livro(isbn, titulo)
        st.success(mensagem)

#Listagem
st.subheader("Lista de Livros Cadastrados")
livros = obter_livros()

if livros:
    for l in livros:
        st.write(f"**ISBN:** {l[0]} | **Título:** {l[1]}")
else:
    st.info("Nenhum livro cadastrado ainda.")

