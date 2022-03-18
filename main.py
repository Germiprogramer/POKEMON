import csv

from classes.pokemon import * 
from classes.pokemon_planta import *


if __name__ == "__main__":
    
    pokemon_1 = Pokemon(1, "bulbasaur", 50, 8, 10)
    pokemon_2 = Pokemon(25, "pikachu", 45, 12, 7)

    combate(pokemon_1, pokemon_2)

