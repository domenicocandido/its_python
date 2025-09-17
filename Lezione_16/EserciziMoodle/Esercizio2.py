class RecipeManager:

    ricette:list[str] = []
    def __init__(self):
        pass

    def create_recipe(self, name:str, ingredients:list[str]) -> dict[str, list[str]]:

        if name not in RecipeManager.ricette:
            RecipeManager.ricette[name] = ingredients
            return {name: ingredients}
        else:
            return 'Errore: la ricetta esiste già'
        
    def add_ingredienti(self,recipe_name:str, ingredient:str):

        if recipe_name in sel():
           if ingredient not in self.nuova_ricetta[recipe_name]:
                self.nuova_ricetta[recipe_name].append(ingredient) 


