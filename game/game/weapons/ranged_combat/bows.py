from .base_weapon import BaseRangetCombat
from random import randint


class SimpleBow(BaseRangetCombat):
    """Класс простые луки"""

    def __init__(self, name, material, shot_power, ammunition, long_shot):
        super().__init__(name, material, shot_power, ammunition, long_shot)

    def not_ammunition(self):
        return 'Стрелы закончилсь!'

    def shot(self):
        self.ammunition -= 1
        return (f'Произведен выстрел из лука {self.name}, '
                f'Осталось {self.ammunition} стрел')


def create_bow_1(full_name):
    bow_1 = SimpleBow('name', 'обычное дерево', 1, 2, 3)
    bow_1.name = full_name
    bow_1.shot_power = randint(5, 10)
    bow_1.ammunition = randint(10, 20)
    bow_1.long_shot = randint(5, 10)
    return bow_1


def create_bow_2(full_name):
    bow_2 = SimpleBow('name', 'хорошее дерево', 1, 2, 3)
    bow_2.name = full_name
    bow_2.shot_power = randint(7, 12)
    bow_2.ammunition = randint(15, 20)
    bow_2.long_shot = randint(7, 12)
    return bow_2
