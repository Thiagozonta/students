import sqlite3
from contextlib import contextmanager

#Constante que indica o caminho para o diretorio do banco de dados
DB_NAME = "C:\Projetos\studentRegistrationSQL\databases\student.db"

def undo(msg:str, e, conexao):
    conexao.rollback()
    print(f"{msg}: {e}")
    raise


@contextmanager
def get_cursor():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    try:
        yield cursor
        conexao.commit()
    except sqlite3.IntegrityError as e:
        undo("ocorreu um erro de integraidade no banco de dados", e, conexao)
    except sqlite3.ProgrammingError as e:
        undo("ocorreu um erro de programacao", e,  conexao)
    except sqlite3.OperationalError as e:
        undo("ocorreu um erro do S. operacional", e, conexao)
    except sqlite3.DatabaseError as e:
        undo("ocorreu um erro de banco de dados:", e, conexao)
    except Exception as e:
        undo("erro inesperado", e, conexao)
    finally:
        conexao.close()

def create_tables():   
    with get_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        age INTEGER
                    )
            """)


 