class Pokemon():
    def __init__(self, ID, pokemon_name, type1, type2, health_points, attack_rating, defense_rating, sp_attack_rating, sp_defense_rating, speed_rating, total, image):
        self.ID = ID
        self.pokemon_name = pokemon_name
        self.type1 = type1
        self.type2 = type2
        self.health_points = health_points
        self.attack_rating = attack_rating
        self.defense_rating = defense_rating
        self.sp_attack_rating = sp_attack_rating
        self.sp_defense_rating = sp_defense_rating
        self.speed_rating = speed_rating
        self.total = total
        self.image = image
        
    def get_ID(self):
        return self.ID

    def set_ID(self, a):
        self.ID = a
    
    def get_pokemon_name(self):
        return self.pokemon_name

    def set_pokemon_name(self, a):
        self.pokemon_name = a

    
    
    def get_type1(self):
        return self.type1

    def set_type1(self, a):
        self.type1 = a

    def get_type2(self):
        return self.type2

    def set_type2(self, a):
        self.type2 = a

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

    def get_sp_attack_rating(self):
        return self.sp_attack_rating

    def set_sp_attack_rating(self, a):
        self.sp_attack_rating = a
    
    def get_sp_defense_rating(self):
        return self.sp_defense_rating

    def set_sp_defense_rating(self, a):
        self.sp_defense_rating = a

    def get_speed_rating(self):
        return self.speed_rating

    def set_speed_rating(self, a):
        self.speed_rating = a

    def get_total(self):
        return self.total

    def set_total(self, a):
        self.total = a
    
    def get_image(self):
        return self.image

    def set_image(self, a):
        self.image = a

    def attack(self, pokemon_2):
        ataque = self.attack_rating-(pokemon_2.get_defense_rating()%2)
        vida = pokemon_2.get_health_points() - ataque
        print("¡{} usa {}!".format(self.pokemon_name, self.nombre_ataque))
        print("¡{} ahora tiene {} puntos de vida!".format(pokemon_2.get_pokemon_name(), vida))
        print("")
        return pokemon_2.set_health_points(vida)

    