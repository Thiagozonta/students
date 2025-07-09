from db.connection import get_cursor
from models.student import Student

def insert_student(student):#inserir 
    with get_cursor() as cursor:
        cursor.execute(
            "INSERT INTO aluno(nome,email,idade) VALUES (?,?,?)",
            (student.name,student.email,student.age)
        )
        
def get_all_students():#pegar
    with get_cursor() as cursor :
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return [Student(id=row[0], name=row[1], email=row[2], age=row[3]) for row in rows ]
    
def update_student(student):#inserir 
    with get_cursor() as cursor:
        cursor.execute( 
            "UPDATE student SET name?, email?, age? WHERE id=? VALUES"
            (student.name,     student.email,    student.age,student.id)
        )
        