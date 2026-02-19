import sqlite3
from tkinter.tix import INTEGER

con = sqlite3.connect('banco.sqlite')
cursor = con.cursor()

def criar_tabela(con, cursor):
    cursor.execute('''CREATE IF NOT EXISTS TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150)
    )''')
    
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
    
excluir_cliente(con, cursor, 1)

