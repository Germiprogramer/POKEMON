import csv

from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *
from eficacias import *

if __name__ == "__main__":
    
    pokemon_1 = Pokemon_planta(1, "bulbasaur", 50, 8, 10)
    pokemon_2 = Pokemon_agua(25, "squirtle", 45, 12, 7)

    eficacias(pokemon_1, pokemon_2)

    combate(pokemon_1, pokemon_2)

