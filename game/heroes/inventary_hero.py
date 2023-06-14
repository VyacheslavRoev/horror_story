from weapons.list_weapons_lev_1 import (training_bow, training_stave,
                                        traning_sword)

traning_inventary = [traning_sword, training_bow, training_stave]


def list_inventary():
    """Вывод инвентаря."""
    for i in traning_inventary:
        print(i)


def get_weapon(index):
    """Выбор оружия в инвентаре."""
    index_weapon = int(index) - 1
    return traning_inventary[index_weapon]
