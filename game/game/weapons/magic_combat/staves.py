from .base_weapon import BaseMagicCombat
from random import randint


class SimpleStave(BaseMagicCombat):
    """Класс простые посохи"""

    def __init__(self, name, material, magic_power, long_shot):
        super().__init__(name, material, magic_power, long_shot)

    def mythical_strike(self):
        return f'Нанесён магический удар посохом {self.name}'


def create_stave_1(full_name):
    stave_1 = SimpleStave('name', 'береза', 1, 2)
    stave_1.name = full_name
    stave_1.magic_power = randint(1, 10)
    stave_1.long_shot = randint(5, 10)
    return stave_1
