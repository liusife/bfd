import sqlite3

DB_name = "biblioteca.db"

def criar_tabela():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS livros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            usuario_cpf TEXT NOT NULL,
            FOREIGN KEY (usuario_cpf) REFERENCES usuarios(cpf)
        );
        
        CREATE TABLE IF NOT EXISTS usuarios (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def conectar_db():
    return sqlite3.connect(DB_name)
