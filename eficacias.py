from classes.pokemon import *
from classes.pokemon_planta import *
from classes.pokemon_electrico import *
from classes.pokemon_agua import *
from classes.pokemon_fuego import *

def eficacias(pokemon_1, pokemon_2):
    if type(pokemon_1).__name__ == "Pokemon_planta" and type(pokemon_2).__name__ == "Pokemon_agua":
        poder_ataque = (pokemon_1.get_attack_rating() * 2)
        pokemon_1.set_attack_rating(poder_ataque)
    if type(pokemon_1).__name__ == "Pokemon_agua" and type(pokemon_2).__name__ == "Pokemon_fuego":
        poder_ataque = (pokemon_1.get_attack_rating() * 2)
        pokemon_1.set_attack_rating(poder_ataque)
    if type(pokemon_1).__name__ == "Pokemon_fuego" and type(pokemon_2).__name__ == "Pokemon_planta":
        poder_ataque = (pokemon_1.get_attack_rating() * 2)
        pokemon_1.set_attack_rating(poder_ataque)
    if type(pokemon_1).__name__ == "Pokemon_electrico" and type(pokemon_2).__name__ == "Pokemon_agua":
        poder_ataque = (pokemon_1.get_attack_rating() * 2)
        pokemon_1.set_attack_rating(poder_ataque)

    if type(pokemon_2).__name__ == "Pokemon_planta" and type(pokemon_1).__name__ == "Pokemon_agua":
        poder_ataque = (pokemon_2.get_attack_rating() * 2)
        pokemon_2.set_attack_rating(poder_ataque)
    if type(pokemon_2).__name__ == "Pokemon_agua" and type(pokemon_1).__name__ == "Pokemon_fuego":
        poder_ataque = (pokemon_2.get_attack_rating() * 2)
        pokemon_2.set_attack_rating(poder_ataque)
    if type(pokemon_2).__name__ == "Pokemon_fuego" and type(pokemon_1).__name__ == "Pokemon_planta":
        poder_ataque = (pokemon_2.get_attack_rating() * 2)
        pokemon_2.set_attack_rating(poder_ataque)
    if type(pokemon_2).__name__ == "Pokemon_electrico" and type(pokemon_1).__name__ == "Pokemon_agua":
        poder_ataque = (pokemon_2.get_attack_rating() * 2)
        pokemon_2.set_attack_rating(poder_ataque)
    else:
        pass
    