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
        return f"{self.name} ({self.primary_type})"
    
# Feed them to increase the health
def feed(self):
        self.hp += 1
#Take a look into it
if __name__ == "__main__":
    print(str(Pokemon(name="aida", primary_type="Dance")) + " :poke as main script")