from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *
from eficacias import *

pokemon_1 = ""
pokemon_2 = ""

entrenador1_pokemon1 = Pokemon_planta(1, "bulbasaur", 50, 8, 10, 9)
entrenador1_pokemon2= Pokemon_agua(4, "squirtle", 45, 9, 11, 10)
entrenador2_pokemon1= Pokemon_fuego(7, "charmander", 47, 11, 7, 11)
entrenador2_pokemon2= Pokemon_electrico(25, "pikachu", 43, 12, 8, 13)

pokemonentrenador1 = [entrenador1_pokemon1, entrenador1_pokemon2]
pokemonentrenador2 = [entrenador2_pokemon1, entrenador2_pokemon2]

print(pokemonentrenador1[0].ID)

def cambio_pok_1(pokemonentrenador1):
    pokemon_1 = pokemonentrenador1[0]
    return pokemon_1

combate(entrenador1_pokemon1, entrenador2_pokemon2)
combate(entrenador1_pokemon2, entrenador2_pokemon2)


#pokemon_1 = cambio_pok_1(pokemonentrenador1[0])
#print(pokemon_1.ID)