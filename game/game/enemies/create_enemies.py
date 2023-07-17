from game.enemies.base_enemy import BaseEnemy
from random import randint
from game.random_number_func import random_phrase
from game.texts.create_enemy.enemy_rus import ENEMY_NAME, ENEMY_PRENAME


def create_name_enemy():
    prename_enemy = random_phrase(ENEMY_PRENAME)
    name_enemy = random_phrase(ENEMY_NAME)
    full_name = prename_enemy + ' ' + name_enemy
    return full_name


def create_enemy_lev_1(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 30, 1)
    enemy.name = full_name
    enemy.health = randint(200, 300)
    enemy.force = randint(1, 10)
    enemy.dexterity = randint(1, 10)
    enemy.protection = randint(1, 10)
    enemy.speed = randint(1, 10)
    enemy.magic = randint(1, 10)
    enemy.lenght = randint(3, 10)
    return enemy


def create_enemy_lev_2(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 50, 2)
    enemy.name = full_name
    enemy.health = randint(250, 350)
    enemy.force = randint(5, 15)
    enemy.dexterity = randint(5, 15)
    enemy.protection = randint(5, 15)
    enemy.speed = randint(5, 15)
    enemy.magic = randint(5, 15)
    enemy.lenght = randint(5, 15)
    return enemy


def create_enemy_lev_3(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 70, 3)
    enemy.name = full_name
    enemy.health = randint(300, 400)
    enemy.force = randint(15, 25)
    enemy.dexterity = randint(15, 25)
    enemy.protection = randint(15, 25)
    enemy.speed = randint(10, 15)
    enemy.magic = randint(10, 15)
    enemy.lenght = randint(5, 20)
    return enemy


def create_enemy_lev_4(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 100, 4)
    enemy.name = full_name
    enemy.health = randint(350, 400)
    enemy.force = randint(25, 30)
    enemy.dexterity = randint(25, 30)
    enemy.protection = randint(25, 30)
    enemy.speed = randint(15, 20)
    enemy.magic = randint(15, 20)
    enemy.lenght = randint(5, 20)
    return enemy
