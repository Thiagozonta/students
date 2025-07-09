import sys
import os

PROJECT_DIR = "C:\\Projetos\\studentRegistrationSQL\\"

sys.path.append(os.path.abspath(PROJECT_DIR))

from db.connection import create_tables
import services.student_service as service

def show_students():
    students = service.display_record()

    for student in students:
        print(f"{student.id} - {student.name} - {student.email} - {student.age}")

#Menu principal
def main_menu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao:str = input("Escolha uma opção:")
    return opcao

if __name__ == "__main__":
    create_tables()    

    while True:
        opcao = main_menu()
        
        if opcao == "1":   
            name:str = input("Nome:")
            email:str = input("E-Mail:")
            age:int = int(input("Idade:"))
            service.create_record(name,email,age)
            show_students()
        #2
        elif opcao == "2":
            show_students()

        #3
        elif opcao == '3':
            student_id = int(input ("ID do aluno a ser atualizado: "))
            name = input("Novo nome: ")
            email = input("Novo email: ")
            age = int(input("Nova idade: "))
            
            service.edit_record(name,email,age,student_id)
            show_students()




        #4
        elif opcao == "5":
            break
        else:
            print("Opcao Invalida")
