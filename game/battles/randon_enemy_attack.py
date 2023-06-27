from battles.close_combat.enemy_attack import enemy_attack_close_combat
from battles.magic_combat.enemy_attack import enemy_attack_magic_combat
from battles.ranged_combat.enemy_attack import enemy_attack_ranged_combat


def enemy_attack(enemy, weapon_enemy, hero):
    """Выбор противником атаки, в зависимости от класса оружия."""
    if weapon_enemy.class_weapon == 'Ближний бой':
        fin = enemy_attack_close_combat(enemy, weapon_enemy, hero)
        return fin
    if weapon_enemy.class_weapon == 'Дальний бой':
        fin = enemy_attack_ranged_combat(enemy, weapon_enemy, hero)
        return fin
    if weapon_enemy.class_weapon == 'Магическое оружие':
        fin = enemy_attack_magic_combat(enemy, weapon_enemy, hero)
        return fin
