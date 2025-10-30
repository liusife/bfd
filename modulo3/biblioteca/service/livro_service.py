from dados.database import conectar_db

def salvar_livro(isbn, titulo, usuario_cpf):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO livros (isbn, titulo, usuario_cpf)
        VALUES (?, ?, ?)
    ''', (isbn, titulo, usuario_cpf))
    conn.commit()
    conn.close()

def listar_livros():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT l.isbn, l.titulo, u.nome
        FROM livros l
        JOIN usuarios u ON l.usuario_cpf = u.cpf
    ''')
    livros = cursor.fetchall()
    conn.close()
    return livros

