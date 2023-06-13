"""Базовый класс оружия ближнего боя."""


class CloseBase:

    def __init__(self, name, material, impact_force):
        """Свойства - название, материал, сила удара, прочность."""
        self.name = name
        self.material = material
        self.impact_force = impact_force
        self.durability = 500

    def sharpen(self):
        """Заточить оружие"""
        self.durability = 500
        return (f'{self.name} заточен.'
                f'Прочность восстановлена.')
