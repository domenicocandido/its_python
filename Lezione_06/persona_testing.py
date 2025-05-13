#dal file persona.py importa la classe Persona
from persona import Persona

dc:Persona = Persona("Domenico", "Candido", 19)
print(dc)
print(dc.name, dc.lastname, dc.age)

# sfrutto la funzione della displaydata delle funzione Persona per visualizzare in output i dati relativi alla persomna dc
dc.displayData()

