from weapons.close_combat.base_weapon import CloseBase


class SimpleSword(CloseBase):

    def __init__(self, name, material, impact_force, injection, blade_length):
        """Добавлены сила укола и длина клинка."""
        super().__init__(name, material, impact_force)
        self.injection = injection
        self.blade_lenght = blade_length

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
            f'{self.name}, длиной {self.blade_lenght} м. '
            f'Класс - {self.class_weapon}. '
            f'Он изготовлен из материала {self.material}, '
            f'Рубящий удар - {self.impact_force}, '
            f'Колющий удар - {self.injection}, '
            f'Прочности осталось - {self.durability} ед.'
        )
