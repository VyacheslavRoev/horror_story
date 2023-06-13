from random import randint


class BaseHero:
    """Базовый класс героя."""

    def __init__(
            self, name, health, force, dexterity,
            endurance, magic, speed
            ):
        """Здоровье, сила, ловкость,
        выносливость, способности к магии, скорость, опыт, уровень."""
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

    def dealing_damage(self, damage):
        """Нанесение урона."""
        effect = (self.force + damage) * randint(0, 10)
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
