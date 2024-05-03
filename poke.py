# Explanation:
#  1.Create a Pokemon
#  2.Take a look into it
#  3.Feed them to increase the health
#  4.Make them battle and decide a winner
#============================================#


#Creating a Pokemone
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        # this one will change:
        self.hp = max_hp
    def __str__(self):
        return f"{self.name} ({self.primary_type} : {self.hp}/{self.max_hp})"
    
# Feed them to increase the health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} now has {self.hp} HP points!")
        else:
            print(f"You have reached max HP points of {self.max_hp}")

# Make them battle and decide a winner
    def battle(self, other):
        print(f"{self.name} VS. {other.name}")
        self.typewheel(self.primary_type,other.primary_type)
        

    @staticmethod
    def typewheel(type1,type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        #map between types and result conditions
        game_map = {"water":0, "fire":1, "grass":2}
        # win-lose matrix:
        wl_matrix=[
            [-1,1,0], #water
            [0,-1,1], #fire
            [1,0,-1]  #grass
        ]

        #declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]
        


#Take a look into it
if __name__ == "__main__":
    print(str(Pokemon(name="aida", primary_type="Dance", max_hp=100)) + " : poke as main script")