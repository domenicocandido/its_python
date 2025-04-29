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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    