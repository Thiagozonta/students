import dao.student_dao as dao
from models.student import Student

def validate_data(student):
    #Validação dos dados
    if student.age >= 130: 
        print("Erro Idade Incorreta")
        return False
    
    #regra de negocio
    if student.age < 10:
        print("Aceitamos matriculas apenas para alunos maiores de idade")
        return False

        #SE RETORNAR TRUE(VDD)DEU TUDO CERTO
    return True


def create_record(name,email,age):
    student = Student(name,email,age)

    if validate_data(student):
        dao.insert_student(student)


def display_record():
    return dao.get_all_students()

def edit_record(name:str, email:str, age:int, id:int):
    student = Student(name, email, age,id)
    
    if validate_data(student):
        dao.update_student(student)

    
    
    