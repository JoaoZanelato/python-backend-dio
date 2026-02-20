import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent # Caminho da pasta onde está o arquivo

con = sqlite3.connect(ROOT_PATH / 'banco.sqlite') #Cria o banco na pasta do arquivo
cursor = con.cursor() 
cursor.row_factory = sqlite3.Row # Ocorre Globalmente no Arquivo

try:
  cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', ('Teste 3', 'teste3@gmail.com'))
  cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?,?,?)', (2, 'Teste 4', 'teste4@gmail.com'))
  con.commit() # Deixar commit dentro do bloco try para ele cair no tratamento de erros correto, sem finally  
except Exception as e:
  print(f'Ops, ocorreu um erro: {e}')
  con.rollback()
