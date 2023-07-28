from game.enemies.random_actions import enemy_random_action
from game.texts.actions import FAR_AWAY, FINISH
from game.texts.attack_messages import DAMAGE, YOU_FAIL, YOU_MAX_DAMAGE


def attack_ranged_combat(weapon, hero, enemy, weapon_enemy, max_health_enemy):
    """Атака оружием дальнего боя."""
    if weapon.long_shot < enemy.lenght:
        print(FAR_AWAY)
        return
    effect = hero.ranged_dealing_damage(weapon.shot_power,
                                        weapon.long_shot, enemy.lenght)
    if effect == 0:
        print(weapon.shot())
        print(YOU_FAIL)
        fin = enemy_random_action(enemy, weapon_enemy, hero,
                                  enemy.lenght, max_health_enemy)
        return fin
    elif effect == ((hero.force + hero.dexterity +
                     weapon.shot_power - enemy.lenght) * 10):
        print(weapon.shot())
        print(YOU_MAX_DAMAGE)
        print(enemy.taking_damage(effect))
        if enemy.health <= 0:
            print(hero.gaining_experience(enemy.experience))
            fin = FINISH
            return fin
    else:
        print(weapon.shot())
        print(DAMAGE)
        print(enemy.taking_damage(effect))
        if enemy.health <= 0:
            print(hero.gaining_experience(enemy.experience))
            fin = FINISH
            return fin
        fin = enemy_random_action(enemy, weapon_enemy, hero,
                                  enemy.lenght, max_health_enemy)
        return fin
