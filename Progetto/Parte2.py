class Person:
     def __init__(self, cf:str, name:str, surname: str, age: int):
         
         self.cf = cf
         self.name = name
         self.surname = surname
         self.age = age
         
class Student(Person):
    
    def __init__(self, cf:str, name:str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group = None
    
    def set_group(self, group:list[str]):
        self.group = group
        
class Lecturer(Person):
    
    def __init__(self, cf:str, name:str, surname: str, age: int):
        super().__init__(cf, name, surname, age)


class Group:
    
    def __init__(self, name:str, limit:int):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    
    def get_name(self):
        return self.name
        
    def get_limit(self):
        return self.limit
        
    def get_students(self):
        return self.students
        
    def get_limit_lecturers(self):
        num_students = len(self.students)
        
        if num_students == 0:
            return 1
        return (num_students + 9) // 10
        
    def add_student(self, student):
        
        if len(self.students) >= self.limit:
            
            print(f"Impossibile aggiungere lo studente {student.name}, nel gruppo \"{self.name}\" è stato raggiunto il limite.")
            return
        self.students.append(student)
        student.set_group(self)
        
    def add_lecturer(self, lecturer):
            
            if len(self.lecturers) >= self.get_limit_lecturers():
                print(f"Impossibile aggiungere il docente {lecturer.name}, nel gruppo \"{self.name}\" è stato raggiunto il limite.")
                return
            
            self.lecturers.append(lecturer)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    