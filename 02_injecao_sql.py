import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent # Caminho da pasta onde está o arquivo

con = sqlite3.connect(ROOT_PATH / 'banco.sqlite') #Cria o banco na pasta do arquivo
cursor = con.cursor() 
cursor.row_factory = sqlite3.Row # Ocorre Globalmente no Arquivo

id_cliente = input('Informe o ID do Cliente: ')
cliente = cursor.execute(f'SELECT * FROM clientes WHERE id ={id_cliente}')
clientes = cursor.fetchall()
for cliente in clientes:
  print(dict(cliente))