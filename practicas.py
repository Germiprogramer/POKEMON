from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *

import pandas as pd

lista_pokemon = pd.read_csv("pokemon_stats(1).csv", header=0)

ID = list(lista_pokemon["ID"])
pokemon_name = list(lista_pokemon["pokemon_name"])
notas_escritura = list(lista_pokemon["writing score percentage"])

charmander = Pokemon()