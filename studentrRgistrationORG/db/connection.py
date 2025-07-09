from peewee import SqliteDatabase
from pathlib import Path #biblioteca para lidar com diretorio para evitar caminhos hard=code

import os 

###RAIZ DO PROJETO###
PROJECT_ROOT = Path(__file__).parent.parent
###ONDE SERÁ CRIADO O BANCO DE DADOS 
DB_DIR = PROJECT_ROOT / "Databases"

###CRIA O DIRETORIO SE ELE NAO EXISTIR###
DB_DIR.mkdir(exist_ok=True)

###CAMINHO COMPLETO PARA O ARQUIVO.db(meu banco de dados)
DB_PATH = DB_DIR / "students02.db"

###CRIA DEFATO O BANCO DE DADOS###
db = SqliteDatabase(DB_PATH)

def connect_db():
    from models.student import Student #importar a classe Students la da pasta models
    db.connect()#abre a conexao com o banco de dados
    db.create_tables([Student], safe=True)


def close_db(exception=None):
        if not db.is_closed():
            db.close()