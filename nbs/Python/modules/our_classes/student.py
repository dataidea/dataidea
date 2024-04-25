from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, id_number, subjects=[]):
        super().__init__(first_name, last_name, age)
        self.id_number = id_number
        self.subjects = subjects

    def addSubject(self, subject):
        self.subjects.append(subject) 

