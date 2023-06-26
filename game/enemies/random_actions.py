from battles.randon_enemy_attack import enemy_attack
from enemies.walking_enemy import walking_enemy_hero
from texts.actions import RUN_ENEMY, WIN


def enemy_random_action(enemy, weapon_enemy,
                        hero, distance, max_health_enemy):
    """Действия противника в зависимости от уровня здоровья."""
    randon_action = enemy.response_action(max_health_enemy)
    if randon_action == 0 and (distance <= weapon_enemy.long_shot):
        enemy_attack(enemy, weapon_enemy, hero)
    elif randon_action == 0 and (distance >= weapon_enemy.long_shot):
        walking_enemy_hero(enemy)
    else:
        print(RUN_ENEMY)
        command = int(input())
        if command == 1:
            return
        elif command == 2:
            print(WIN)
            return command
