import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
con = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = con.cursor()

def criar_tabela(con, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150)
    )''')
    con.commit()
    
def inserir_cliente(con, cursor, nome, email):
    data = (nome, email)
    cursor.execute('''INSERT INTO clientes (nome, email) VALUES
        (?,?)''', data)
    con.commit()
    
def update_cliente(con, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute('''UPDATE clientes SET nome=?, email=? WHERE id=?''', data)
    con.commit()

def excluir_cliente(con, cursor, id):
    data = (id,) 
    cursor.execute('''DELETE FROM clientes WHERE id=?''', data)
    con.commit()

def inserir_muitos(con, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) values (?,?)", dados)
    con.commit()

def recuperar_cliente_por_id(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome')

cliente = recuperar_cliente_por_id(cursor, 4)
print(cliente)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
