# from weapons.list_weapons_lev_1 import traning_sword
from enemies.list_enemies_lev_1 import training_enemy
from .actions import INVENTARY, YES, NO  # HACK, PRICK, ENDURANCE, HERO,


COMMAND = 'Введите команду: '
NEW_TRAINING = (f'Если хотите начать тренировку наберите на клавиатуре '
                f'"{YES}", для пропуска "{NO}"')
MESSAGE_NEW_TRAINING = (
    f'''Тренировка началась. Ваш противник - {training_enemy.name}
Выберите оружие. Для этого введите номер оружия в инвентаре.
Для просмотра инвентаря введите {INVENTARY}
Для выхода из тренировки - {NO}''')

MESSAGE_REPEAT_TRAINING = (f'Если хотите повторить тренировку наберите '
                           f'клавиатуре "{YES}", для завершения "{NO}"')
END_TRAINING = 'Тренировка окончена'


# У вас в руках {traning_sword}
# Для рубящего удара введите команду - "{HACK}"
# Для колющего удара введите команду - "{PRICK}"
# Для проверки прочности оружия введите - "{ENDURANCE}"
# Для просмотра параметров героя введите - "{HERO}"
