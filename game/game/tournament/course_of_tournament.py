from game.battles.close_combat.preparing_for_battle import get_close_weapon
from game.battles.magic_combat.preparing_for_battle import get_magic_weapon
from game.battles.ranged_combat.preparing_for_battle import get_ranged_weapon
from game.texts.attack_messages import WEAPON_FAIL
from game.texts.tournament_messages import TOURNAMENT_WEAPON
from game.texts.actions import COMMAND, ERROR_LIST, FINISH, FAIL
from game.random_number_func import random_phrase


def battle(hero, hero_weapon, enemy, enemy_weapon,
           max_health_enemy):
    new_battle = ''
    while new_battle != '0':
        if enemy_weapon.durability <= 0:
            print(WEAPON_FAIL)
            return FINISH
        if enemy_weapon.ammunition <= 0:
            print(enemy_weapon.not_ammunition())
            return FINISH
        print(f"""{TOURNAMENT_WEAPON}
        1 - {hero_weapon[0]}
        2 - {hero_weapon[1]}
        3 - {hero_weapon[2]}

        0 - Выход""")
        new_battle = input(COMMAND)
        if new_battle == '1':
            fin = get_close_weapon(
                new_battle, hero,
                enemy, enemy_weapon, max_health_enemy, hero_weapon)
            if fin == FINISH:
                return fin
            if fin == FAIL:
                return fin
        if new_battle == '2':
            fin = get_ranged_weapon(
                new_battle, hero,
                enemy, enemy_weapon, max_health_enemy, hero_weapon)
            if fin == FINISH:
                return fin
            if fin == FAIL:
                return fin
        if new_battle == '3':
            fin = get_magic_weapon(
                new_battle, hero,
                enemy, enemy_weapon, max_health_enemy, hero_weapon
            )
            if fin == FINISH:
                return fin
            if fin == FAIL:
                return fin
        if new_battle == '0':
            print('BYE!!!')
        else:
            print(random_phrase(ERROR_LIST))


def break_battle(hero, hero_weapon, max_health_hero):
    print('br bt')
