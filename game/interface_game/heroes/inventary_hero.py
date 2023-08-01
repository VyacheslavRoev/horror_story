def list_inventary(inventary):
    """Вывод инвентаря."""
    pass


def get_weapon(index, inventary):
    """Выбор оружия в инвентаре."""
    index_weapon = int(index) - 1
    return inventary[index_weapon]
