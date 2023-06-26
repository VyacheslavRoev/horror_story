class BaseRangetCombat:
    """Базовый класс оружия дальнего боя."""

    def __init__(self, name, material, shot_power, ammunition, long_shot):
        """Название, материал, сила выстрела, количество боеприпасов,
          дальность выстрела, класс оружия, прочность"""
        self.name = name
        self.material = material
        self.shot_power = shot_power
        self.ammunition = ammunition
        self.long_shot = long_shot
        self.class_weapon = 'Дальний бой'
        self.durability = 100

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
            f'Сила выстрела - {self.shot_power}. '
            f'Дальность выстрела - {self.long_shot}. '
            f'Осталось {self.ammunition} стрел.')
