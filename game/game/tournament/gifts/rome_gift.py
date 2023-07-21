from random import randint

from database.db import (delete_weapon_hero, insert_weapon, return_hero_id,
                         return_id_weapon, update_hero)

from game.texts.actions import COMMAND
from game.texts.tournament_messages import GIFT, NO_THANKS, THANKS
from game.weapons.close_combat.swords import SimpleSword
from game.weapons.magic_combat.staves import SimpleStave
from game.weapons.ranged_combat.bows import SimpleBow

sword = SimpleSword('Имперский меч', 'дамасская сталь', 35, 20)
bow = SimpleBow('Имперский лук', 'составная кость', 25, 20, 20)
stave = SimpleStave('Имперский посох', 'кости животных и серебро',
                    20, 15)


def rome_tournament_gift(hero, weapons, max_health_hero):
    """Подарок римского императора."""
    hero_id = return_hero_id(hero.name)
    hero.rome = 1
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
            max_health_hero += 70
            hero.force += 10
            hero.dexterity += 10
            hero.magic += 10
            hero.speed += 10
        else:
            print(NO_THANKS)
    elif random_gift == 5:
        print('Имперская броня')
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            hero.protection += 20
        else:
            print(NO_THANKS)
    values = (max_health_hero, hero.force,
              hero.dexterity, hero.magic, hero.speed,
              hero.protection, hero.experience, hero.tsar,
              hero.teutonic, hero.polovistan, hero.rome,
              hero.persia, hero.barbarians, hero_id)
    update_hero(values)
