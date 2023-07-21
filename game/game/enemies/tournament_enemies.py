from game.weapons.create_weapon import (create_name_weapon,
                                        create_weapon_lev_1,
                                        create_weapon_lev_2,
                                        create_weapon_lev_3,
                                        create_weapon_lev_4,
                                        create_weapon_lev_5,
                                        create_weapon_lev_6,
                                        create_weapon_lev_7)

from .create_enemies import (create_enemy_lev_1, create_enemy_lev_2,
                             create_enemy_lev_3, create_enemy_lev_4,
                             create_enemy_lev_5, create_enemy_lev_6,
                             create_enemy_lev_7, create_name_enemy)


def preparation_enemy_1():
    """Подготовка противника 1 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_1(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_1(weapon_full_name)
    return enemy, weapon


def preparation_enemy_2():
    """Подготовка противника 2 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_2(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_2(weapon_full_name)
    return enemy, weapon


def preparation_enemy_3():
    """Подготовка противника 3 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_3(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_3(weapon_full_name)
    return enemy, weapon


def preparation_enemy_4():
    """Подготовка противника 4 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_4(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_4(weapon_full_name)
    return enemy, weapon


def preparation_enemy_5():
    """Подготовка противника 5 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_5(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_5(weapon_full_name)
    return enemy, weapon


def preparation_enemy_6():
    """Подготовка противника 6 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_6(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_6(weapon_full_name)
    return enemy, weapon


def preparation_enemy_7():
    """Подготовка противника 7 уровня."""
    full_name = create_name_enemy()
    enemy = create_enemy_lev_7(full_name)
    weapon_full_name = create_name_weapon()
    weapon = create_weapon_lev_7(weapon_full_name)
    return enemy, weapon