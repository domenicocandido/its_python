class Room:
    def __init__(self, id:int, floor:int, seats:int):
        
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2
        
    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor
        
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area
        
class Building:
    def __init__ (self, name:str, address:str, floors:list[int]):
        
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
        
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
        
    def add_room(self, room):
        
        if self.floors[0] <= room.get_floor() <= self.floors[1]:
            if room not in self.rooms:
                self.rooms.append(room)
    
    def area(self):
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area

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
            
class Course:
    
    def __init__(self,name:str ):
        self.name = name
        self.groups = []
        
    def register(self, student:str):
        
        for group in self.groups:
            
            if len(group.get_students()) < group.get_limit():
                
                group.add_student(student)
                return
            print(f"Non ci sono posti disponibili in nessi gruppo per lo studente {student.name}")
    
    def get_groups(self):
        return self.groups
    
    def add_group(self, group):
        self.groups.append(group)