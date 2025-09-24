from film import Film
from movie_genre import *

class Noleggio:

    def __init__(self, film_list:list[Film]):
        
        self.film_list = []
        self.rented_film = {}
    
    def isAvaible(self, film):
        return film in self.film_list
    