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
    bow = SimpleBow('name', 'обычное дерево', 1, 2, 3)
    bow.name = full_name
    bow.shot_power = randint(5, 10)
    bow.ammunition = randint(10, 20)
    bow.long_shot = randint(5, 10)
    return bow


def create_bow_2(full_name):
    bow = SimpleBow('name', 'хорошее дерево', 1, 2, 3)
    bow.name = full_name
    bow.shot_power = randint(7, 12)
    bow.ammunition = randint(15, 20)
    bow.long_shot = randint(7, 12)
    return bow


def create_bow_3(full_name):
    bow = SimpleBow('name', 'прочное дерево', 1, 2, 3)
    bow.name = full_name
    bow.shot_power = randint(9, 14)
    bow.ammunition = randint(15, 20)
    bow.long_shot = randint(9, 12)
    return bow


def create_bow_4(full_name):
    bow = SimpleBow('name', 'железное дерево', 1, 2, 3)
    bow.name = full_name
    bow.shot_power = randint(10, 15)
    bow.ammunition = randint(15, 20)
    bow.long_shot = randint(10, 14)
    return bow


def create_bow_5(full_name):
    bow = SimpleBow('name', 'чёрное дерево', 1, 2, 3)
    bow.name = full_name
    bow.shot_power = randint(15, 20)
    bow.ammunition = randint(15, 20)
    bow.long_shot = randint(15, 20)
    return bow
