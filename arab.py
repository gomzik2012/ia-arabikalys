from character import Character
import random
popoi = random.randint(1,65)
class Arabian(Character):



    def __init__(self, name, health=100, damage=20, defense=0):
        Character.__init__(self, name, health=150, damage=40, defense=0)

    def attack(self, target):
        final_damage = 1 * 1000 if popoi == 1 else self.damage
        return target.take_damage(final_damage)