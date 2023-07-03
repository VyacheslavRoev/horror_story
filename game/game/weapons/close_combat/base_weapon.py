"""Базовый класс оружия ближнего боя."""
from game.weapons.base_weapon import WeaponBase


class CloseBase(WeaponBase):

    def __init__(self, name, material, impact_force):
        """Название, материал, сила удара,
        прочность, класс оружия, количество зарядов"""
        super().__init__(name, material)
        self.impact_force = impact_force
        self.shot_power = 0
        self.magic_power = 0
        self.class_weapon = 'Ближний бой'
        self.ammunition = 1
        self.long_shot = 1

    def sharpen(self):
        """Заточить оружие"""
        self.durability = 500
        return (f'{self.name} заточен.'
                f'Прочность восстановлена.')

    def get_weapon_enemy(self):
        """Информация об оружии противника."""
        return (f'{self.name}, '
                f'Изготовленный из материала - {self.material}, '
                f'Класс оружия - {self.class_weapon}.')
