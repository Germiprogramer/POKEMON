from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *

import pandas as pd

lista_pokemon = pd.read_csv("pokemon_stats (1).csv", header=0)

ID = list(lista_pokemon["ID"])
pokemon_name = list(lista_pokemon["pokemon_name"])
type1 = list(lista_pokemon["Type1"])
type2 = list(lista_pokemon["Type2"])
hp = list(lista_pokemon["HP"])
attack = list(lista_pokemon["Attack"])
defense = list(lista_pokemon["Defense"])
sp_attack = list(lista_pokemon["SpAttack"])
sp_defense = list(lista_pokemon["SpDefense"])
speed = list(lista_pokemon["Speed"])
total = list(lista_pokemon["Total"])
image = list(lista_pokemon["Image"])
