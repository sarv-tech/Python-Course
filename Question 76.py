# Q. Create a class Player with :
# • a class variable player_count
# • instance variables name and level 
# Track how many players were created.


class Player:
    player_count = 0         # class variable to track total players

    def __init__(self, name, level):
        self.name = name              # instance variable for player name
        self.level = level            # instance variable for player level
        Player.player_count += 1

# Creating Object 
p1 = Player("Sarvesh", 2)             
p2 = Player("Rohan", 3)
p3 = Player("Sana", 5)

print(p1.name, p1.level)
print(p2.name, p2.level)
print(p3.name, p3.level)

print(f"Total player Created = {Player.player_count}")           # total players created