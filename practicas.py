from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *
from combate import *
from eficacias import *

entrenador1_pokemon1 = Pokemon_planta(1, "bulbasaur", 50, 8, 10, 9)
entrenador1_pokemon2= Pokemon_agua(4, "squirtle", 45, 9, 11, 10)
entrenador2_pokemon1= Pokemon_fuego(7, "charmander", 47, 11, 7, 11)
entrenador2_pokemon2= Pokemon_electrico(25, "pikachu", 43, 12, 8, 13)

pokemonentrenador1 = [entrenador1_pokemon1, entrenador1_pokemon2]
pokemonentrenador2 = [entrenador2_pokemon1, entrenador2_pokemon2]

def combateconcambio(pokemonentrenador1, pokemonentrenador2):
    i = 0
    j = 0

    if pokemonentrenador1[i].get_health_points() <0:
        i = i + 1
    if pokemonentrenador2[j].get_health_points() <0:
        j = j + 1


    
    pokemonentrenador1[i].eficacias(pokemonentrenador2[j])
    pokemonentrenador2[j].eficacias(pokemonentrenador1[i])
    combate(pokemonentrenador1[i], pokemonentrenador2[j])
    if pokemonentrenador1[i].get_health_points() >0 and pokemonentrenador2[j].get_health_points()>0:
        try:
            combateconcambio(pokemonentrenador1, pokemonentrenador2)
        except:
            pass
    else:
        pass

combateconcambio(pokemonentrenador1, pokemonentrenador2)