import csv

from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *
from eficacias import *

pokemon_1 = Pokemon_planta(1, "bulbasaur", 50, 8, 10)
pokemon_2 = Pokemon_agua(4, "squirtle", 45, 12, 7)

pokemon_2.attack(pokemon_1)
print(pokemon_1.health_points)