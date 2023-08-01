from .actions import YES, NO


NEW_TRAINING = 'ЖЕЛАЕТЕ НАЧАТЬ ТРЕНИРОВКУ?'
NEW_TRAINING_BT_1 = 'Начать'
NEW_TRAINING_BT_2 = 'Вывести информацию о герое'
NEW_TRAINING_BT_3 = 'Посмотреть инвентарь'
NEW_TRAINING_BT_4 = 'Вернуться в главное меню'

GET_ENEMY = 'ВЫБЕРИТЕ СВОЕГО ПРОТИВНИКА'
GET_ENEMY_BT_1 = 'Рекрут с мечом'
GET_ENEMY_BT_2 = 'Рекрут с луком'
GET_ENEMY_BT_3 = 'Ученик колдуна'

NEXT = 'Продолжить'

BACK = 'Вернуться в предыдущее меню'

NEW_WEAPON = 'Сменить оружие'

GET_TRAINING_WEAPON = 'ВЫБЕРИТЕ ОРУЖИЕ'
GET_TRAINING_WEAPON_BT_1 = 'Тренировочный меч'
GET_TRAINING_WEAPON_BT_2 = 'Тренировочный лук'
GET_TRAINING_WEAPON_BT_3 = 'Жезл ученика'

MESSAGE_NEW_TRAINING = (
    '''
    ТРЕНИРОВКА НАЧАЛАСЬ!'''
)

MESSAGE_REPEAT_TRAINING = (f'Если хотите повторить тренировку наберите '
                           f'клавиатуре "{YES}", для завершения "{NO}"')
END_TRAINING = ('''
    ТРЕНИРОВКА ОКОНЧЕНА!''')
