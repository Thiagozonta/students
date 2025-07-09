#Esse programa é do tipo procedure --> procedural: variaveis e funcoes
import sqlite3

#########################################
#   Definicao de Variaveis Globais
#########################################

#########################################
### Definicao de funcoes 
#########################################
def main_menu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao:str = input("Escolha uma opção:")
    return opcao

def create_table():
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    idade INTEGER
                   )
        """)
    conexao.commit()    
    conexao.close()

def register(nome:str,email:str,idade:int):
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO aluno(nome,email,idade) VALUES (?,?,?)",
                       (nome,email,idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Email ja cadastrado")        
    finally:
        conexao.close()

       

def display():
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db") #abrir na conexao com o banco 
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno")  #FLULL TABLE SCAN 
    alunos = cursor.fetchall()

    conexao.close() #fecho a conexao com o banco 

    print("Lista de Alunos cadastrados")

    for aluno in alunos:
        print(aluno)

def delete(id):
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db") #abrir na conexao com o banco 
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM aluno WHERE id = ?",
                   (id))
    
    conexao.commit()
    conexao.close()
    print("Aluno deletado com sucesso!!")
def update(id,new_nome,new_email,new_idade):
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db") #abrir na conexao com o banco 
    cursor = conexao.cursor()

    cursor.execute("UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
                   (new_nome,new_email,new_idade,id))
    
    conexao.commit()
    conexao.close()
    print("Aluno atualizado com sucesso")


if __name__ == "__main__":
    create_table()    

    while True:
        opcao = main_menu()
        
        if opcao == "1": 
            nome:str = input("Nome:")
            email:str = input("E-Mail:")
            idade:int = int(input("Idade:"))
            register(nome,email,idade)
        elif opcao == "2":
            display()
        elif opcao == "3":
            id = int(input("Informe o ID do Aluno que vc quer atualizar"))
            new_nome = input("Novo Nome")
            new_email = input("Novo E-mail")
            new_idade = int(input("Nova idade"))
            update(id,new_nome,new_email,new_idade)
        elif opcao == "5":
            break
        elif opcao == "4":
            id = input("Informe o ID do Aluno que vc quer deletar:")
            delete(id)        
        else:
            print("Opcao Invalida")
            


    

    
    
    