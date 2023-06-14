from .base_enemy import BaseEnemy


training_enemy = BaseEnemy(
    'Рекрут с мечом', 250, 10, 10, 1, 10, 0, 10, 50, 1
    )
training_enemy_2 = BaseEnemy(
    'Рекрут с луком', 250, 10, 10, 1, 10, 0, 10, 50, 1
    )
training_enemy_3 = BaseEnemy(
    'Ученик колдуна', 250, 10, 10, 1, 10, 10, 10, 50, 1
    )

list_training_enemy = [training_enemy, training_enemy_2, training_enemy_3]


def get_training_enemy(index):
    """Выбор противника для тренировки."""
    index_enemy = int(index) - 1
    return list_training_enemy[index_enemy]
