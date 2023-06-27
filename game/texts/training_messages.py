from .actions import YES, NO


NEW_TRAINING = (
    """
    ЖЕЛАЕТЕ НАЧАТЬ ТРЕНИРОВКУ?
    1 - Начать
    2 - Вывести информацию о герое
    3 - Посмотреть инвентарь
    0 - Вернуться в главное меню
    """
)
GET_ENEMY = (
    '''
    ВЫБЕРИТЕ ПРОТИВНИКА ИЗ СПИСКА:
    1 - Рекрут с мечом
    2 - Рекрут с луком
    3 - Ученик колдуна
    '''
)
GET_TRAINING_WEAPON = (
    '''
    ВЫБЕРИТЕ ОРУЖИЕ:
    1 - Тренировочный меч
    2 - Тренировочный лук
    3 - Жезл ученика

    0 - Выход из тренировки
    '''
)
MESSAGE_NEW_TRAINING = (
    '''
    ТРЕНИРОВКА НАЧАЛАСЬ!'''
)

MESSAGE_REPEAT_TRAINING = (f'Если хотите повторить тренировку наберите '
                           f'клавиатуре "{YES}", для завершения "{NO}"')
END_TRAINING = ('''
    ТРЕНИРОВКА ОКОНЧЕНА!''')
