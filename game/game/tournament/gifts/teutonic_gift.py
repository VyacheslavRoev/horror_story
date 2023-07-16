from random import randint

from database.db import (delete_weapon_hero, insert_weapon, return_hero_id,
                         return_id_weapon, update_hero)

from game.texts.actions import COMMAND
from game.texts.tournament_messages import GIFT, NO_THANKS, THANKS
from game.weapons.close_combat.swords import SimpleSword
from game.weapons.magic_combat.staves import SimpleStave
from game.weapons.ranged_combat.bows import SimpleBow

sword = SimpleSword('Тевтонский меч', 'отличная сталь с позолотой', 20, 10)
bow = SimpleBow('Тевтонский лук', 'крепкий дуб с позолотой', 18, 20, 15)
stave = SimpleStave('Тевтонский магический посох', 'чёрное дерево', 15, 15)


def teutonic_tournament_gift(hero, weapons):
    """Подарок царя."""
    hero_id = return_hero_id(hero.name)
    random_gift = randint(1, 5)
    if random_gift == 1:
        print(sword)
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            if weapons[0] is not None:
                weapon_id = return_id_weapon(weapons[0].name, hero_id)
                delete_weapon_hero(weapon_id)
            values_weapon = (
                    sword.name, sword.material,
                    sword.impact_force,
                    sword.injection, sword.shot_power,
                    sword.magic_power, sword.class_weapon,
                    sword.ammunition, sword.long_shot,
                    sword.durability, hero_id
                )
            insert_weapon(values_weapon)
        else:
            print(NO_THANKS)
    elif random_gift == 2:
        print(bow)
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            if weapons[1] is not None:
                weapon_id = return_id_weapon(weapons[1].name, hero_id)
                delete_weapon_hero(weapon_id)
            values_weapon = (
                    bow.name, bow.material,
                    bow.impact_force,
                    bow.injection, bow.shot_power,
                    bow.magic_power, bow.class_weapon,
                    bow.ammunition, bow.long_shot,
                    bow.durability, hero_id
                )
            insert_weapon(values_weapon)
        else:
            print(NO_THANKS)
    elif random_gift == 3:
        print(stave)
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            if weapons[2] is not None:
                weapon_id = return_id_weapon(weapons[2].name, hero_id)
                delete_weapon_hero(weapon_id)
            values_weapon = (
                    stave.name, stave.material,
                    stave.impact_force,
                    stave.injection, stave.shot_power,
                    stave.magic_power, stave.class_weapon,
                    stave.ammunition, stave.long_shot,
                    stave.durability, hero_id
                )
            insert_weapon(values_weapon)
        else:
            print(NO_THANKS)
    elif random_gift == 4:
        print('Волшебное кольцо')
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            hero.health += 50
            hero.force += 5
            hero.dexterity += 5
            hero.magic += 5
            hero.speed += 5
            values = (hero.health, hero.force,
                      hero.dexterity, hero.magic, hero.speed, hero_id)
            update_hero(values)
        else:
            print(NO_THANKS)
    elif random_gift == 5:
        print('Рыцарская броня')
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            hero.protection += 10
            values = (hero.protection, hero_id)
            update_protection_hero(values)
        else:
            print(NO_THANKS)
