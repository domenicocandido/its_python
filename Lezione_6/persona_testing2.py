# dal file persona2 importa la classe Persona
from persona2 import Persona

dc:Persona = Persona()

dc.displayData()
print("----------------")

#imposto il nome della persona dc
dc.setName("Domenico")
dc.displayData()

#imposto il cognome della persona dc
dc.setLastname("Candido")

#imposto l'età della persona dc
dc.setAge(29)

print("--------------")

dc.displayData()

print("-------------")

print(dc.getName(), dc.getLastname(), dc.getAge())






