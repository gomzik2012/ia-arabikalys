from character import Character
from arab import Arabian

player1 = Character("Kirill", 225, 77, 0)
player1.print_stats()

player2 = Arabian("Arabian", 425, 70, 0)
player2.print_stats()

print("\n\n")
player1.print_stats()
player2.print_stats()

player1.attack(player2)

print("\n")


while player1.health > 0 and player2.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} напав {player2.name}  наніс {player1_damage} шкоди")
    print(f"{player2.name} залишилося {player2.health}  здоров'я")
    player2_damage = player2.attack(player1)
    print(f"{player2.name} напав {player1.name}  наніс {player2_damage-player1.defense} шкоди")
    print(f"{player1.name} залишилося {player1.health}  здоров'я")
    print("")