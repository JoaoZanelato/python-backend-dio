import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # Caminho da pasta onde está o arquivo

con = sqlite3.connect(ROOT_PATH / "banco.sqlite")  # Cria o banco na pasta do arquivo
cursor = con.cursor()
cursor.row_factory = sqlite3.Row  # Ocorre Globalmente no Arquivo


def tratamento_de_erro(func):
    def wrapper(*args, **kwargs):
        try:
            print("---------------------------------")
            print("INICIANDO OPERAÇÃO...")

            # Executa a função
            resultado = func(*args, **kwargs)

            print(" OPERAÇÃO REALIZADA COM SUCESSO!")
            print("---------------------------------\n")

            return resultado

        except Exception as e:
            print(f"Erro: {e}")
            print("---------------------------------\n")

    return wrapper


@tratamento_de_erro
def criar_tabela(con, cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS pessoa_fisica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150),
    cpf CHAR(11)
    )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS pessoa_juridica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150),
    cnpj CHAR(14)
    )"""
    )
    con.commit()


criar_tabela(con, cursor)


@tratamento_de_erro
def inserir_pessoa_fisica(con, cursor, nome, email, cpf):
    data = (nome, email, cpf)
    cursor.execute(
        """INSERT INTO pessoa_fisica (nome, email, cpf) VALUES
            (?,?,?)""",
        data,
    )
    con.commit()


@tratamento_de_erro
def inserir_pessoa_juridica(con, cursor, nome, email, cnpj):
    data = (nome, email, cnpj)
    cursor.execute(
        """INSERT INTO pessoa_juridica (nome, email, cnpj) VALUES
            (?,?,?)""",
        data,
    )
    con.commit()


@tratamento_de_erro
def update_pessoa_fisica(con, cursor, id, nome, email, cpf):
    data = (nome, email, cpf, id)
    cursor.execute(
        """UPDATE pessoa_fisica SET nome=?, email=?, cpf=? WHERE id=?""", data
    )
    con.commit()


@tratamento_de_erro
def update_pessoa_juridica(con, cursor, id, nome, email, cnpj):
    data = (nome, email, cnpj, id)
    cursor.execute(
        """UPDATE pessoa_juridica SET nome=?, email=?, cnpj=? WHERE id=?""", data
    )
    con.commit()


@tratamento_de_erro
def excluir_pessoa_fisica(con, cursor, id):
    data = (id,)
    cursor.execute("""DELETE FROM pessoa_fisica WHERE id=?""", data)
    con.commit()


@tratamento_de_erro
def excluir_pessoa_juridica(con, cursor, id):
    data = (id,)
    cursor.execute("""DELETE FROM pessoa_juridica WHERE id=?""", data)
    con.commit()


@tratamento_de_erro
def recuperar_pessoa_fisica_por_id(cursor, id):
    cursor.execute("SELECT * FROM pessoa_fisica WHERE id = ?", (id,))
    return dict(cursor.fetchone())


@tratamento_de_erro
def recuperar_pessoa_juridica_por_id(cursor, id):
    cursor.execute("SELECT * FROM pessoa_juridica WHERE id = ?", (id,))
    return dict(cursor.fetchone())


@tratamento_de_erro
def listar_pessoas_fisicas(cursor):
    return cursor.execute("SELECT * FROM pessoa_fisica ORDER BY nome")


@tratamento_de_erro
def listar_pessoas_juridicas(cursor):
    return cursor.execute("SELECT * FROM pessoa_juridica ORDER BY nome")


rodar = True

while rodar:
    print(
        "BEM VINDO AO SISTEMA DE GERENCIAMENTO DE USUÁRIOS\nINSIRA O NÚMERO CORRESPONDENTE A OPERAÇÃO\nINSERIR PESSOA FISICA - 1\nINSERIR PESSOA JURIDICA - 2\nALTERAR PESSOA FISICA - 3\nALTERAR PESSOA JURIDICA - 4\nEXCLUIR PESSOA FISICA - 5\nEXCLUIR PESSOA JURIDICA - 6\nRECUPERAR PESSOA FISICA POR ID - 7\nRECUPERAR PESSOA JURIDICA POR ID - 8\nLISTAR PESSOAS FISICAS - 9\nLISTAR PESSOAS JURIDICAS - 10\nSAIR - 0"
    )
    opcao = int(input("OPÇÃO: "))
    match opcao:
        case 1:
            nome = input("NOME: ")
            email = input("EMAIL: ")
            cpf = input("CPF: ")
            inserir_pessoa_fisica(con, cursor, nome, email, cpf)
        case 2:
            nome = input("NOME: ")
            email = input("EMAIL: ")
            cnpj = input("CNPJ: ")
            inserir_pessoa_juridica(con, cursor, nome, email, cnpj)
        case 3:
            id = int(input("ID DA PESSOA FISICA: "))
            nome = input("NOVO NOME: ")
            email = input("NOVO EMAIL: ")
            cpf = input("NOVO CPF: ")
            update_pessoa_fisica(con, cursor, id, nome, email, cpf)
        case 4:
            id = int(input("ID DA PESSOA JURIDICA: "))
            nome = input("NOVO NOME: ")
            email = input("NOVO EMAIL: ")
            cnpj = input("NOVO CNPJ: ")
            update_pessoa_juridica(con, cursor, id, nome, email, cnpj)

        case 5:
            id = int(input("ID DA PESSOA FISICA A EXCLUIR: "))
            excluir_pessoa_fisica(con, cursor, id)
        case 6:
            id = int(input("ID DA PESSOA JURIDICA A EXCLUIR: "))
            excluir_pessoa_juridica(con, cursor, id)
        case 7:
            id = int(input("ID DA PESSOA FISICA A RECUPERAR: "))
            pessoa_fisica = recuperar_pessoa_fisica_por_id(cursor, id)
            print(pessoa_fisica)
        case 8:
            id = int(input("ID DA PESSOA JURIDICA A RECUPERAR: "))
            pessoa_juridica = recuperar_pessoa_juridica_por_id(cursor, id)
            print(pessoa_juridica)
        case 9:
            pessoas_fisicas = listar_pessoas_fisicas(cursor)
            for pessoa in pessoas_fisicas:
                print(dict(pessoa))
        case 10:
            pessoas_juridicas = listar_pessoas_juridicas(cursor)
            for pessoa in pessoas_juridicas:
                print(dict(pessoa))
        case 0:
            rodar = False
            print("SAINDO DO SISTEMA...")
