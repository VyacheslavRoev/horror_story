from game.texts.attack_messages import DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE


def enemy_attack_ranged_combat(enemy, weapon, hero):
    """Атака противником оружием дальнего боя."""
    effect = enemy.ranged_dealing_damage(weapon.shot_power,
                                         weapon.long_shot, enemy.lenght)
    print(f'{enemy.name} пытается выстрелить.')
    if effect == 0:
        print(weapon.shot())
        print(f'{enemy.name} {ENEMY_FAIL}')
    elif effect == ((enemy.force + enemy.dexterity +
                     weapon.shot_power - enemy.lenght) * 10):
        print(weapon.shot())
        print(ENEMY_MAX_DAMAGE)
        print(hero.taking_damage(effect))
        if hero.health <= 0:
            return
        enemy_attack_ranged_combat(enemy, weapon, hero)
    else:
        print(weapon.shot())
        print(DAMAGE)
        print(hero.taking_damage(effect))