from .base_weapon import BaseMagicCombat
from random import randint


class SimpleStave(BaseMagicCombat):
    """Класс простые посохи"""

    def __init__(self, name, material, magic_power, long_shot):
        super().__init__(name, material, magic_power, long_shot)

    def mythical_strike(self):
        return f'Нанесён магический удар посохом {self.name}'


def create_stave_1(full_name):
    stave = SimpleStave('name', 'береза', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(1, 10)
    stave.long_shot = randint(5, 10)
    return stave


def create_stave_2(full_name):
    stave = SimpleStave('name', 'осина', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(5, 10)
    stave.long_shot = randint(5, 10)
    return stave


def create_stave_3(full_name):
    stave = SimpleStave('name', 'липа', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(8, 13)
    stave.long_shot = randint(7, 11)
    return stave


def create_stave_4(full_name):
    stave = SimpleStave('name', 'дуб', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(10, 15)
    stave.long_shot = randint(7, 12)
    return stave


def create_stave_5(full_name):
    stave = SimpleStave('name', 'красное дерево', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(15, 17)
    stave.long_shot = randint(10, 15)
    return stave


def create_stave_6(full_name):
    stave = SimpleStave('name', 'кость с изумрудным навершием', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(20, 23)
    stave.long_shot = randint(10, 15)
    return stave


def create_stave_7(full_name):
    stave = SimpleStave('name', 'кость с рубиновым навершием', 1, 2)
    stave.name = full_name
    stave.magic_power = randint(20, 25)
    stave.long_shot = randint(10, 15)
    return stave
