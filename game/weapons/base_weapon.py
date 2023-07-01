"""Базовый класс оружия."""


class WeaponBase:

    def __init__(self, name, material):
        """Свойства - название, материал, сила удара,
        сила выстрела, сила магического воздействия,
        класс оружия, количество зарядов, дальность поражения,
        прочность."""
        self.name = name
        self.material = material
        self.durability = 500
