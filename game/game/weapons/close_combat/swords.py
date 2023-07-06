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
    sword_1 = SimpleSword('name', 'сталь', 1, 2)
    sword_1.name = full_name
    sword_1.impact_force = randint(5, 10)
    sword_1.injection = randint(1, 5)
    return sword_1
