from .base_weapon import BaseRangetCombat


class SimpleBow(BaseRangetCombat):
    """Класс простые луки"""

    def __init__(self, name, material, shot_power, ammunition, long_shot):
        super().__init__(name, material, shot_power, ammunition, long_shot)

    def not_ammunition(self):
        return 'Стрелы закончилсь!'

    def shot(self):
        self.ammunition -= 1
        return (f'Произведен выстрел из лука {self.name}, '
                f'Осталось {self.ammunition} стрел')
