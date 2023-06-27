from texts.attack_messages import ENEMY_FAIL, ENEMY_MAX_DAMAGE, DAMAGE
from texts.actions import FINISH


def enemy_attack_close_combat(enemy, weapon, hero):
    """Атака противником оружием ближнего боя."""
    effect = enemy.close_dealing_damage(weapon.impact_force)
    print(f'{enemy.name} пытается нанести удар.')
    if effect == 0:
        print(f'{enemy.name} {ENEMY_FAIL}')
    elif effect == (enemy.force + weapon.impact_force) * 10:
        damage = hero.taking_damage(effect)
        print(weapon.slashing_blow())
        print(ENEMY_MAX_DAMAGE)
        print(damage)
        if damage == 'Вы убиты!':
            fin = FINISH
            return fin
        fin = enemy_attack_close_combat(enemy, weapon, hero)
        if fin == FINISH:
            return fin
    else:
        print(weapon.slashing_blow())
        print(DAMAGE)
        print(hero.taking_damage(effect))
        if hero.health <= 0:
            fin = FINISH
            return fin
