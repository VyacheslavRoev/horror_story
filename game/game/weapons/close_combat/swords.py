from .base_weapon import CloseBase
from random import randint


class SimpleSword(CloseBase):

    def __init__(self, name, material, impact_force, injection):
        super().__init__(name, material, impact_force, injection)

    def slashing_blow(self):
        """Рубящий удар."""
        self.durability -= 30
        return (f'Нанесен рубящий удар мечем {self.name}. '
                f'Прочность снижена на 20 ед.')

    def stabbing_blow(self):
        """Колющий удар."""
        self.durability -= 10
        return (f'Нанесен колющий удар мечем {self.name}. '
                f'Прочность снижена на 10 ед.')

    def __str__(self):
        return (
            f'{self.name}. '
            f'Класс - {self.class_weapon}. '
            f'Он изготовлен из материала {self.material}, '
            f'Рубящий удар - {self.impact_force}, '
            f'Колющий удар - {self.injection}, '
            f'Прочности осталось - {self.durability} ед.'
        )


def create_sword_1(full_name):
    sword = SimpleSword('name', 'сталь', 1, 2)
    sword.name = full_name
    sword.impact_force = randint(10, 15)
    sword.injection = randint(5, 10)
    return sword


def create_sword_2(full_name):
    sword = SimpleSword('name', 'хорошая сталь', 1, 2)
    sword.name = full_name
    sword.impact_force = randint(12, 17)
    sword.injection = randint(5, 10)
    return sword


def create_sword_3(full_name):
    sword = SimpleSword('name', 'очень хорошая сталь', 1, 2)
    sword.name = full_name
    sword.impact_force = randint(15, 20)
    sword.injection = randint(7, 12)
    return sword


def create_sword_4(full_name):
    sword = SimpleSword('name', 'отличная сталь', 1, 2)
    sword.name = full_name
    sword.impact_force = randint(17, 23)
    sword.injection = randint(10, 15)
    return sword
