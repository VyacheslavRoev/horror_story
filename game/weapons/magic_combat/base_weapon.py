class BaseMagicCombat:
    """Базовый класс магического оружия."""

    def __init__(self, name, material, magic_power, long_shot):
        """Названиеб материал, сила удара, дальность поражения
        класс оружия"""
        self.name = name
        self.material = material
        self.magic_power = magic_power
        self.long_shot = long_shot
        self.class_weapon = 'Магическое оружие'

    def __str__(self):
        return (
            f'{self.name}. '
            f'Класс - {self.class_weapon}. '
            f'Изготовлен из материала {self.material}. '
            f'Сила удара - {self.magic_power}. '
            f'Дальность поражения - {self.long_shot}.')
