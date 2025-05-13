class Restaurant:
    def __init__(self, name:str, cuisine_type:str):
        self.name = name
        self.cuisine_type= cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self) -> None:
          
        msg =  f"Al ristorante \"{self.name}\" si mangia {self.cuisine_type}."
        print(msg)
     
    def open_restaurant(self) -> None:

        msg = f"Il ristorante \"{self.name}\" è aperto. Venite da noi."
        print(msg)

    def set_number_served(self, number_served:int) -> None :

        self.number_served = number_served
    
    def increment_number_served(self, new_clients) -> None:

        self.number_served += new_clients




restaurant = Restaurant("Bottarolo", "pasta")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")

restaurant.number_served = 200
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(50) 
print(f"Number served: {restaurant.number_served}")