

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

