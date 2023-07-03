from .base_weapon import CloseBase


class SimpleSword(CloseBase):

    def __init__(self, name, material, impact_force, injection):
        """Добавлены дальность поражения, сила укола и длина клинка."""
        super().__init__(name, material, impact_force)
        self.long_shot = 1
        self.injection = injection

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
