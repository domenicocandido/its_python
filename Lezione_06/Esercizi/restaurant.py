class Restaurant:
     def __init__(self, name:str, cuisine_type:str):
          self.name = name
          self.cuisine_type= cuisine_type
    
     def describe_restaurant(self) -> None:
          
          msg =  f"Al ristorante \"{self.name}\" si mangia {self.cuisine_type}."
          print(msg)
     
     def open_restaurant(self) -> None:

          msg = f"Il ristorante \"{self.name}\" è aperto. Venite da noi."
          print(msg)

restaurant = Restaurant('Bottarolo', 'pasta')
print(restaurant.name) 
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()