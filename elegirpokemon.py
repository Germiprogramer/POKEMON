from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *
from listas_datos import *

import pandas as pd

lista_pokemon = pd.read_csv("pokemon_stats (1).csv", header=0)

def elegirpokemon(nombre, pokemon):
    pokemon = Pokemon(ID[pokemon_name.index(nombre)], pokemon_name[pokemon_name.index(nombre)], type1[pokemon_name.index(nombre)], type2[pokemon_name.index(nombre)], hp[pokemon_name.index(nombre)], attack[pokemon_name.index(nombre)], defense[pokemon_name.index(nombre)], sp_attack[pokemon_name.index(nombre)], sp_defense[pokemon_name.index(nombre)], speed[pokemon_name.index(nombre)], total[pokemon_name.index(nombre)], image[pokemon_name.index(nombre)])
    return pokemon

entrenador1_pokemon1 = None

elegirpokemon("Charizard", entrenador1_pokemon1)

entrenador1_pokemon1.get_type1()

#esto esta mal

