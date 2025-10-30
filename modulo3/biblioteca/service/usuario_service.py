from dados.database import conectar_db

def salvar_usuario(usuario):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (cpf, nome)
        VALUES (?, ?)
    ''', (usuario.cpf, usuario.nome))
    conn.commit()
    conn.close()

def autenticar_usuario(cpf):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT cpf, nome FROM usuarios WHERE cpf = ?', (cpf,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

