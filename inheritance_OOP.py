class Student:
    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
class CFGStudent(Student):
    def __init__(self, name, age,id, subjects,specialisation):
        super().__init__(name, age, id, subjects)
        self.subjects = subjects
        self.average_mark = 0
        self.specialisation = specialisation
#cause thats how you start off in OOP and the  super().__init__ (xxx) use that when you want to inherit (edited) 
