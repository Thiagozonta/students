#essa classe/Objeto aluno é paradigma OO Orientado à Objetos

class Student:
    
    #metodo construtor da classe Aluno/Student e ele é um metodo especial
    def __init__(self,name,email,age,id=None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age        
    
    def __repr__(self):
        return f"Student(id={self.id}, Name={self.name}, Email={self.email}, Age={self.age})"
    
