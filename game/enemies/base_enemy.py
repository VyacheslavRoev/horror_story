from random import randint


class BaseEnemy:
    """Базовый класс врага"""

    def __init__(self, name, health, force, dexterity,
                 protection, speed, magic, lenght, experience, level):
        """Имя, здоровье, сила, ловкость,
        защита, скорость, способности к магии,
        расстояние до врага, опыт за врага, уровень"""
        self.name = name
        self.health = health
        self.force = force
        self.dexterity = dexterity
        self.protection = protection
        self.speed = speed
        self.magic = magic
        self.lenght = lenght
        self.experience = experience
        self.level = level

    def max_health(self):
        """Максимальное здоровье."""
        max_health_enemy = self.health
        return max_health_enemy

    def death(self):
        """Смерть."""
        return f'{self.name} убит!'

    def distance(self, steps):
        """Изменение расстояния до противника."""
        self.lenght -= steps
        if self.lenght == 0:
            self.lenght = 1
        return self.lenght

    def taking_damage(self, damage):
        """Получение урона."""
        full_damage = (damage - self.protection -
                       (self.dexterity * randint(0, 5)))
        if full_damage < 0:
            full_damage = 0
        self.health -= full_damage
        if self.health <= 0:
            return self.death()
        return (f'{self.name} получил урон {full_damage}. '
                f'У него осталось {self.health} ед. здоровья.')

    def magic_taking_damage(self, damage):
        """Получение урона магией."""
        self.health -= damage
        if self.health <= 0:
            return self.death()
        return (f'{self.name} получил урон {damage}. '
                f'У него осталось {self.health} ед. здоровья.')

    def close_dealing_damage(self, damage):
        """Нанесение урона оружием ближнего боя."""
        effect = (self.force + damage) * randint(0, 10)
        return effect

    def ranged_dealing_damage(self, damage, long_shot, lenght):
        """Нанесение урона оружием дальнего боя"""
        if lenght > long_shot:
            self.walking()
        else:
            effect = ((self.force + self.dexterity + damage - lenght) *
                      randint(0, 10))
            return effect

    def magic_dealing_damage(self, damage, long_shot, lenght, magic_health):
        """Нанесение урона магическим оружием."""
        if lenght > long_shot:
            self.walking()
        self.health -= magic_health
        effect = ((magic_health * 3) + self.magic + damage) // (randint(1, 10))
        return effect

    def response_action(self, max_health):
        """Ответное действие."""
        if self.health <= max_health / 10:
            random_action = randint(0, 2)
        else:
            random_action = 0
        return random_action

    def enemy_info(self):
        """Информация о противнике."""
        return (
            f'''имя - {self.name}
            здоровье - {self.health}
            сила - {self.force}
            ловкость - {self.dexterity}
            защита - {self.protection}
            скорость - {self.speed}
            способности к магии - {self.magic}
            расстояние до врага - {self.lenght}
            уровень - {self.level}
            '''
        )

    def __str__(self):
        return (f'{self.name}, здоровье - {self.health}, '
                f'уровень - {self.level}')
