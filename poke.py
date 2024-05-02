# Explanation:
#  1.Create a Pokemon
#  2.Take a look into it
#  3.Feed them to increase the health
#  4.Make them battle and decide a winner
#============================================#


#Creating a Pokemone
class Pokemon:
    def __init__(self, name, primary_type):
        self.name = name
        self.primary_type = primary_type
    def __str__(self):
        return f"{self.name} ({self.primary_type})"
#Take a look into it

print()