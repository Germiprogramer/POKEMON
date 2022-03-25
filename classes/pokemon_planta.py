from classes.pokemon import * 

class Pokemon_planta(Pokemon):
    nombre_ataque = "hoja afilada"
    def eficacias(self, pokemon_2):
        if type(pokemon_2).__name__ == "Pokemon_agua":
            self.attack_rating = self.attack_rating * 2
        else:
            pass
        return self.attack_rating
