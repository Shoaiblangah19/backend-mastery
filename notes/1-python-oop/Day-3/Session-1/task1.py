
### ⚡ Micro Task 1 (7 min)

# Predict the output of this code WITHOUT running it. Then run it to verify:


class Player:
    game_name = "Battle Arena"
    max_health = 100
    player_count = 0
    
    def __init__(self, name: str):
        self.name = name
        self.health = Player.max_health
        Player.player_count += 1

p1 = Player("Ali")
p2 = Player("Sara")

print(Player.player_count)    # 2
print(p1.player_count)        # 2
print(p2.player_count)        # 2

p1.max_health = 200

print(p1.max_health)          # 200
print(p2.max_health)          # 100
print(Player.max_health)      # 100

print(p1.health)              # 100
print(p2.health)              # 100

Player.game_name = "Super Arena"
print(p1.game_name)           # Super Arena
print(p2.game_name)           # Super Arena