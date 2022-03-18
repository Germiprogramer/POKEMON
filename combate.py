from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *


def attackpokemon_1(pokemon_1, pokemon_2):
    ataque1 = pokemon_1.get_attack_rating()-(pokemon_2.get_defense_rating()%2)
    vida = pokemon_2.get_health_points() - ataque1
    print("¡{} usa {}!".format(pokemon_1.get_pokemon_name(), pokemon_1.nombre_ataque))
    print("¡{} ahora tiene {} puntos de vida!".format(pokemon_2.get_pokemon_name(), vida))
    print("")
    return pokemon_2.set_health_points(vida)

def attackpokemon_2(pokemon_1, pokemon_2):
    ataque2 = pokemon_2.get_attack_rating()-(pokemon_1.get_defense_rating()%2)
    vida = pokemon_1.get_health_points() - ataque2
    print("¡{} usa {}!".format(pokemon_2.get_pokemon_name(), pokemon_2.nombre_ataque))
    print("¡{} ahora tiene {} puntos de vida!".format(pokemon_1.get_pokemon_name(), vida))
    print("")
    return pokemon_1.set_health_points(vida)

def combate(pokemon_1, pokemon_2):
    attackpokemon_1(pokemon_1, pokemon_2)
    attackpokemon_2(pokemon_1, pokemon_2)
    if pokemon_1.get_health_points() >0 and pokemon_2.get_health_points()>0:
        combate(pokemon_1, pokemon_2)
    else:
        if pokemon_1.get_health_points() <=0:
            print("{} se ha debilitado, la victoria es para {}".format(pokemon_1.get_pokemon_name(),pokemon_2.get_pokemon_name()))
        if pokemon_2.get_health_points() <=0:
            print("{} se ha debilitado, la victoria es para {}".format(pokemon_2.get_pokemon_name(),pokemon_1.get_pokemon_name()))
