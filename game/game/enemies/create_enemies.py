from game.enemies.base_enemy import BaseEnemy
from random import randint


def create_enemy_lev_1(full_name):
    enemy_1 = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 100, 1)
    enemy_1.name = full_name
    enemy_1.health = randint(200, 300)
    enemy_1.force = randint(1, 10)
    enemy_1.dexterity = randint(1, 10)
    enemy_1.protection = randint(1, 10)
    enemy_1.speed = randint(1, 10)
    enemy_1.magic = randint(1, 10)
    enemy_1.lenght = randint(5, 20)
    return enemy_1
