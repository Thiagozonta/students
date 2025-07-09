import sys
from pathlib import Path
###PEGA O CAMINHO DO ARQUIVO ATUAL,NO CASO (MAIN.PY)###
current_File = Path(__file__)

###DEFINE RAIZ DO PROJETO###
project_root = Path(__file__).parent.parent

###ADICIONA A RAIZ DO PROJETO "PATH" DO PYTHON###
sys.path.append(str(project_root))




from db.connection import connect_db, close_db
from services.student_service import StudentService
def show_menu():
    print("\n=== Sistema de cadastro de alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar ALuno")
    print ("5.Sair")
    print("---------------------")

def main():
    connect_db()

    service = StudentService()

    while True:
        show_menu()

        opcao = input("Escolha uma opção:")

        if opcao == "1":
            print("Aluno Cadastrado com Sucesso")
            name = input("Informe o nome Aluno:")
            age = input("Infrome a idade Aluno:")
            email = input("Informe o email Aluno:")

            service.register_student(name,age,email)

            print("Aluno cadastrado com Sucesso!")

        elif opcao == "2":
            print("Alunos com Cadastros foram listados com sucesso")
            


        elif opcao == "5":
            print("Saindo do Sistema")
            break
        else :
            print ("Opcao invalida")

    close_db()

if __name__=="__main__":
    main()