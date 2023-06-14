from random import randint


class BaseHero:
    """Базовый класс героя."""

    def __init__(
            self, name, health, force, dexterity,
            endurance, magic, speed
            ):
        """Здоровье, сила, ловкость,
        выносливость, способности к магии,
        скорость, защита, опыт, уровень."""
        self.name = name
        self.health = health
        self.force = force
        self.dexterity = dexterity
        self.endurance = endurance
        self.magic = magic
        self.speed = speed
        self.protection = 1
        self.experience = 0
        self.level = 1

    def death(self):
        """Смерть."""
        return 'Вы убиты!'

    def walking(self):
        """Шагать."""
        # Написать функцию
        pass

    def taking_damage(self, damage):
        """Получение урона."""
        full_damage = (damage - self.protection -
                       (self.dexterity * randint(0, 5)))
        if full_damage < 0:
            full_damage = 0
        self.health -= full_damage
        if self.health <= 0:
            return self.death()
        return (f'Вы получили урон {full_damage}. '
                f'Осталось {self.health} ед. здоровья.')

    def magic_taking_damage(self, damage):
        """Получение урона магией."""
        self.health -= damage
        if self.health <= 0:
            return self.death()
        return (f'Вы получили урон {damage}. '
                f'Осталось {self.health} ед. здоровья.')

    def close_dealing_damage(self, damage):
        """Нанесение урона оружием ближнего боя."""
        effect = (self.force + damage) * randint(0, 10)
        return effect

    def ranged_dealing_damage(self, damage, long_shot, lenght):
        """Нанесение урона оружием дальнего боя"""
        if lenght > long_shot:
            return ('Слишком большое расстояние для выстрела! '
                    'Подойдите ближе!')
        effect = ((self.force + self.dexterity + damage - lenght) *
                  randint(0, 10))
        return effect

    def magic_dealing_damage(self, damage, long_shot, lenght, magic_health):
        """Нанесение урона магическим оружием."""
        if lenght > long_shot:
            return ('Слишком большое расстояние! '
                    'Подойдите ближе!')
        self.health -= magic_health
        effect = ((magic_health * 3) + self.magic + damage) // (randint(1, 5))
        return effect

    def __str__(self):
        return f'''
Параметры вашего героя:
имя - {self.name}
здоровье - {self.health}
сила - {self.force}
ловкость - {self.dexterity}
выносливость - {self.endurance}
способности к магии - {self.magic}
скорость - {self.speed}
защита - {self.protection}
опыт - {self.experience}
уровень - {self.level}'''
