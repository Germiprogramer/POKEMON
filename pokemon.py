class Pokemon():
    def __init__(self, ID, pokemon_name, health_points, attack_rating, defense_rating):
        self.ID = ID
        self.pokemon_name = pokemon_name
        self.health_points = health_points
        self.attack_rating = attack_rating
        self.defense_rating = defense_rating
        
    def get_ID(self):
        return self.ID

    def set_ID(self, a):
        self.age = a
    
    def get_pokemon_name(self):
        return self.pokemon_name

    def set_pokemon_name(self, a):
        self.pokemon_name = a

    def get_health_points(self):
        return self.health_points

    def set_health_points(self, a):
        self.health_points = a
    
    def get_attack_rating(self):
        return self.attack_rating

    def set_attack_rating(self, a):
        self.attack_rating = a
    
    def get_defense_rating(self):
        return self.defense_rating

    def set_defense_rating(self, a):
        self.defense_rating = a
    

pokemon_1 = Pokemon(1, "bulbasaur", 50, 8, 10)
pokemon_2 = Pokemon(25, "pikachu", 45, 12, 7)

def attackpokemon_1(pokemon_1, pokemon_2):
    ataque1 = pokemon_1.get_attack_rating()
    vida = pokemon_2.get_health_points() - ataque1
    print("¡{} ATACA!".format(pokemon_1.get_pokemon_name()))
    print("¡{} ahora tiene {} puntos de vida!".format(pokemon_2.get_pokemon_name(), vida))
    print("")
    return pokemon_2.set_health_points(vida)

def attackpokemon_2(pokemon_1, pokemon_2):
    ataque2 = pokemon_2.get_attack_rating()
    vida = pokemon_1.get_health_points() - ataque2
    print("¡{} ATACA!".format(pokemon_2.get_pokemon_name()))
    print("¡{} ahora tiene {} puntos de vida!".format(pokemon_1.get_pokemon_name(), vida))
    print("")
    return pokemon_1.set_health_points(vida)

def combate(pokemon_1, pokemon_2):
    attackpokemon_1(pokemon_1, pokemon_2)
    attackpokemon_2(pokemon_1, pokemon_2)
    if pokemon_1.get_health_points() >0 and pokemon_2.get_health_points()>0:
        combate(pokemon_1, pokemon_2)
    else:
        if pokemon_1.get_health_points() <0:
            print("{} se ha debilitado, la victoria es para {}".format(pokemon_1.get_pokemon_name(),pokemon_2.get_pokemon_name()))
        if pokemon_2.get_health_points() <0:
            print("{} se ha debilitado, la victoria es para {}".format(pokemon_2.get_pokemon_name(),pokemon_1.get_pokemon_name()))


combate(pokemon_1, pokemon_2)

attackpokemon_1(pokemon_1, pokemon_2)

print(pokemon_2.get_health_points())




