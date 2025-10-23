import sqlite3

DB_name = "livros.db"

def criar_tabela():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def conectar_db():
    return sqlite3.connect(DB_name)
