from random import randint


class BaseEnemy:
    """Базовый класс врага"""

    def __init__(self, name, health, force, dexterity,
                 protection, speed, lenght, experience, level):
        """Имя, здоровье, сила, ловкость,
        защита, скорость, расстояние до врага, опыт за врага, уровень"""
        self.name = name
        self.health = health
        self.force = force
        self.dexterity = dexterity
        self.protection = protection
        self.speed = speed
        self.lenght = lenght
        self.experience = experience
        self.level = level

    def death(self):
        """Смерть."""
        return f'{self.name} убит!'

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
