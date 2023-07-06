from game.enemies.base_enemy import BaseEnemy
from random import randint


def create_enemy_lev_1(full_name):
    enemy_1 = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 30, 1)
    enemy_1.name = full_name
    enemy_1.health = randint(200, 300)
    enemy_1.force = randint(1, 10)
    enemy_1.dexterity = randint(1, 10)
    enemy_1.protection = randint(1, 10)
    enemy_1.speed = randint(1, 10)
    enemy_1.magic = randint(1, 10)
    enemy_1.lenght = randint(5, 20)
    return enemy_1


def create_enemy_lev_2(full_name):
    enemy_2 = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 50, 2)
    enemy_2.name = full_name
    enemy_2.health = randint(250, 350)
    enemy_2.force = randint(5, 15)
    enemy_2.dexterity = randint(5, 15)
    enemy_2.protection = randint(5, 15)
    enemy_2.speed = randint(5, 15)
    enemy_2.magic = randint(5, 15)
    enemy_2.lenght = randint(5, 20)
    return enemy_2
