from battles.close_combat.hero_attack import attack_close_combat
# from battles.magic_combat.hero_attack import attack_magic_combat
# from battles.ranged_combat.hero_attack import attack_ranged_combat
# from texts.actions import MAGIC_HEALTH


def hero_attack(enemy, weapon_enemy, weapon_hero, hero, magic_health):
    if weapon_hero.class_weapon == 'Ближний бой':
        attack_close_combat(1, weapon_hero, hero, enemy, weapon_enemy)
    # elif weapon_hero.class_weapon == 'Дальний бой':
    #     attack_ranged_combat(weapon_hero, hero, enemy, weapon_enemy)
    # elif weapon_hero.class_weapon == 'Магическое оружие':
    #     magic_health = int(input(MAGIC_HEALTH))
    #     attack_magic_combat(weapon_hero, hero, enemy,
    #                         weapon_enemy, magic_health)
