from random import randint

from database.db import (delete_weapon_hero, insert_weapon, return_hero_id,
                         return_id_weapon, update_hero)

from game.texts.actions import COMMAND
from game.texts.tournament_messages import GIFT, NO_THANKS, THANKS
from game.weapons.close_combat.swords import SimpleSword
from game.weapons.magic_combat.staves import SimpleStave
from game.weapons.ranged_combat.bows import SimpleBow

tsar_sword = SimpleSword('Царский меч', 'отличная сталь с позолотой', 30, 12)
tsar_bow = SimpleBow('Царский лук', 'крепкий дуб с позолотой', 20, 20, 15)
tsar_stave = SimpleStave('Царский магический посох',
                         'крепкий дуб с позолотой', 15, 15)


def tournament_tsar_gift(hero, weapons, max_health_hero):
    """Подарок царя."""
    hero_id = return_hero_id(hero.name)
    hero.tsar = 1
    random_gift = randint(1, 5)
    if random_gift == 1:
        print(tsar_sword)
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            if weapons[0] is not None:
                weapon_id = return_id_weapon(weapons[0].name, hero_id)
                delete_weapon_hero(weapon_id)
            values_weapon = (
                    tsar_sword.name, tsar_sword.material,
                    tsar_sword.impact_force,
                    tsar_sword.injection, tsar_sword.shot_power,
                    tsar_sword.magic_power, tsar_sword.class_weapon,
                    tsar_sword.ammunition, tsar_sword.long_shot,
                    tsar_sword.durability, hero_id
                )
            insert_weapon(values_weapon)
        else:
            print(NO_THANKS)
    elif random_gift == 2:
        print(tsar_bow)
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            if weapons[1] is not None:
                weapon_id = return_id_weapon(weapons[1].name, hero_id)
                delete_weapon_hero(weapon_id)
            values_weapon = (
                    tsar_bow.name, tsar_bow.material,
                    tsar_bow.impact_force,
                    tsar_bow.injection, tsar_bow.shot_power,
                    tsar_bow.magic_power, tsar_bow.class_weapon,
                    tsar_bow.ammunition, tsar_bow.long_shot,
                    tsar_bow.durability, hero_id
                )
            insert_weapon(values_weapon)
        else:
            print(NO_THANKS)
    elif random_gift == 3:
        print(tsar_stave)
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            if weapons[2] is not None:
                weapon_id = return_id_weapon(weapons[2].name, hero_id)
                delete_weapon_hero(weapon_id)
            values_weapon = (
                    tsar_stave.name, tsar_stave.material,
                    tsar_stave.impact_force,
                    tsar_stave.injection, tsar_stave.shot_power,
                    tsar_stave.magic_power, tsar_stave.class_weapon,
                    tsar_stave.ammunition, tsar_stave.long_shot,
                    tsar_stave.durability, hero_id
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
            max_health_hero += 50
            hero.force += 5
            hero.dexterity += 5
            hero.magic += 5
            hero.speed += 5
        else:
            print(NO_THANKS)
    elif random_gift == 5:
        print('Царская броня')
        print(GIFT)
        gift = input(COMMAND)
        if gift == '1':
            print(THANKS)
            hero.protection += 10
        else:
            print(NO_THANKS)
    values = (max_health_hero, hero.force,
              hero.dexterity, hero.magic, hero.speed,
              hero.protection, hero.experience, hero.tsar,
              hero.teutonic, hero.polovistan, hero.rome,
              hero.persia, hero.barbarians, hero.koschei, hero_id)
    update_hero(values)
