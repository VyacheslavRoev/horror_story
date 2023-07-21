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
    enemy.health = randint(400, 500)
    enemy.force = randint(15, 25)
    enemy.dexterity = randint(15, 25)
    enemy.protection = randint(15, 25)
    enemy.speed = randint(5, 15)
    enemy.magic = randint(15, 20)
    enemy.lenght = randint(5, 20)
    return enemy


def create_enemy_lev_4(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 80, 4)
    enemy.name = full_name
    enemy.health = randint(500, 600)
    enemy.force = randint(30, 35)
    enemy.dexterity = randint(30, 35)
    enemy.protection = randint(30, 35)
    enemy.speed = randint(5, 20)
    enemy.magic = randint(25, 30)
    enemy.lenght = randint(5, 20)
    return enemy


def create_enemy_lev_5(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 100, 5)
    enemy.name = full_name
    enemy.health = randint(600, 800)
    enemy.force = randint(50, 60)
    enemy.dexterity = randint(50, 60)
    enemy.protection = randint(50, 60)
    enemy.speed = randint(5, 20)
    enemy.magic = randint(30, 40)
    enemy.lenght = randint(5, 20)
    return enemy


def create_enemy_lev_6(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 120, 6)
    enemy.name = full_name
    enemy.health = randint(800, 1000)
    enemy.force = randint(60, 70)
    enemy.dexterity = randint(60, 70)
    enemy.protection = randint(60, 70)
    enemy.speed = randint(5, 20)
    enemy.magic = randint(35, 50)
    enemy.lenght = randint(5, 20)
    return enemy


def create_enemy_lev_7(full_name):
    enemy = BaseEnemy('name', 100, 5, 5, 5, 5, 5, 5, 140, 7)
    enemy.name = full_name
    enemy.health = randint(1200, 1500)
    enemy.force = randint(70, 80)
    enemy.dexterity = randint(70, 80)
    enemy.protection = randint(70, 80)
    enemy.speed = randint(5, 20)
    enemy.magic = randint(40, 50)
    enemy.lenght = randint(5, 20)
    return enemy
