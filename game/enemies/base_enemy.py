from random import randint


class BaseEnemy:
    """Базовый класс врага"""

    def __init__(self, name, health, force, dexterity,
                 protection, speed, experience, level):
        """Имя, здоровье, сила, ловкость,
        защита, скорость, опыт за врага, уровень"""
        self.name = name
        self.health = health
        self.force = force
        self.dexterity = dexterity
        self.protection = protection
        self.speed = speed
        self.experience = experience
        self.level = level

    def death(self):
        """Смерть."""
        return f'{self.name} убит!'

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
    
    def dealing_damage(self, damage):
        """Нанесение урона."""
        effect = (self.force + damage) * randint(0, 10)
        return effect
