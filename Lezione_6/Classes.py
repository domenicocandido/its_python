class Person:
   
   def __init__(self, name, age):       
    self.name = name       
    self.age = age 
    
    
alice = Person("Alice W.", 45) 
bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:
  print(alice.name)

else:
  print(bob.name)


kenan = Person("Kenan", 19)
giuseppe = Person("Giuseppe", 27)
pasquale = Person("Pasquale", 20)

people:list[Person] = [alice, bob, kenan, giuseppe, pasquale]


min:int = alice.age
min_name = alice.name

for person in people:
  if person.age < min:
    min = person.age
    min_name = person.name

print(f"La persona con l'età minore è: {min_name}")