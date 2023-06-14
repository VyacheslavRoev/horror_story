from .base_weapon import BaseMagicCombat


class SimpleStave(BaseMagicCombat):
    """Класс простые посохи"""

    def __init__(self, name, material, magic_power, long_shot):
        super().__init__(name, material, magic_power, long_shot)

    def mythical_strike(self):
        return f'Нанесён магический удар посохом {self.name}'
