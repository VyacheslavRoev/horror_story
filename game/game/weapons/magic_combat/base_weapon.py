from game.weapons.base_weapon import WeaponBase


class BaseMagicCombat(WeaponBase):
    """Базовый класс магического оружия."""

    def __init__(self, name, material, magic_power, long_shot):
        """Название, материал, сила удара, дальность поражения
        класс оружия, прочность, количество зарядов"""
        super().__init__(name, material)
        self.magic_power = magic_power
        self.long_shot = long_shot
        self.impact_force = 0
        self.shot_power = 0
        self.class_weapon = 'Магическое оружие'
        self.ammunition = 1
        self.injection = 0

    def get_weapon_enemy(self):
        """Информация об оружии противника."""
        return (f'{self.name}, '
                f'Изготовленный из материала - {self.material}, '
                f'Класс оружия - {self.class_weapon}.')

    def __str__(self):
        return (
            f'{self.name}. '
            f'Класс - {self.class_weapon}. '
            f'Изготовлен из материала {self.material}. '
            f'Сила удара - {self.magic_power}. '
            f'Дальность поражения - {self.long_shot}.')
