'''
### ⚡ Micro Task 3 (8 min)

Create a `Player` class for a simple game with name, health (starts at 100), and attack power.

Write these methods:
- `take_damage(amount)` — reduce health (minimum 0, can't go negative)
- `heal(amount)` — increase health (maximum 100, can't exceed)
- `is_alive()` — True if health > 0
- `attack(other_player)` — deals THIS player's attack power as damage to the OTHER player. Should call the other player's `take_damage()` method.

Create 2 players with different attack powers. Have them attack each other a few times. Print health after each attack. Keep attacking until one dies (is_alive returns False).

This tests: methods modifying state, methods calling other methods, and methods operating on other objects.

'''

class Player:
    def __init__(self,name:str,health:int,attack_power:int):
        self.name:str = name
        self.health:int = health
        self.attack_power:int = attack_power
    
    def take_damage(self,amount:int)->None:
        self.health -= amount
        if self.health<0:
            self.health = 0

    def heal(self,amount:int)->None:
        self.health += amount
        if self.health>100:
            self.health=100
    
    def is_alive(self)->bool:
        return self.health>0
    
    def attack(self,Other:object)->None:
        Other.take_damage(self.attack_power)


if __name__ == "__main__":
    # Test initialization (will pass if syntax is fixed)
    try:
        player = Player("Test", 100, 20)
        assert player.name == "Test"
        assert player.health == 100
        assert player.attack_power == 20
        print("Initialization test passed.")
    except Exception as e:
        print(f"Initialization test failed: {e}")

    # Test take_damage with valid reduction (will pass if syntax is fixed)
    try:
        player = Player("TestDamage", 100, 0)
        player.take_damage(30)
        assert player.health == 70
        print("Take damage test passed.")
    except Exception as e:
        print(f"Take damage test failed: {e}")

    # Test take_damage equal to health (will FAIL due to ValueError)
    try:
        player = Player("TestEqual", 50, 0)
        player.take_damage(50)  # Should NOT raise error, but code does
        assert player.health == 0
        print("Equal damage test passed.")
    except Exception as e:
        print(f"Equal damage test failed: {e}")

    # Test heal (will FAIL due to AttributeError from 'self.heal')
    try:
        player = Player("TestHeal", 80, 0)
        player.heal(30)  # Fails here due to typo
        assert player.health == 100
        print("Heal test passed.")
    except Exception as e:
        print(f"Heal test failed: {e}")

    # Test attack method (will pass if syntax is fixed)
    try:
        att = Player("Attacker", 100, 15)
        deft = Player("Defender", 100, 0)
        att.attack(deft)
        assert deft.health == 85
        print("Attack test passed.")
    except Exception as e:
        print(f"Attack test failed: {e}")

    # Battle test (will FAIL due to take_damage errors)
    print("\nBattle Test:")
    try:
        p1 = Player("Warrior", 100, 10)
        p2 = Player("Mage", 100, 15)
        round_num = 1
        while p1.is_alive() and p2.is_alive():
            print(f"Round {round_num}:")
            p1.attack(p2)
            print(f"Mage health: {p2.health}")
            if not p2.is_alive():
                break
            p2.attack(p1)
            print(f"Warrior health: {p1.health}")
            if not p1.is_alive():
                break
            round_num += 1
        print(f"Winner: {p1.name if p1.is_alive() else p2.name}!")
    except Exception as e:
        print(f"Battle test failed: {e}")