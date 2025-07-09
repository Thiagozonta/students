from models.student import Student

class StudentDAO:
    def create(self, name,age,email):
        return Student.create(name=name, age=age, email=email)