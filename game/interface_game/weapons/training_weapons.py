from .close_combat.swords import SimpleSword
from .ranged_combat.bows import SimpleBow
from .magic_combat.staves import SimpleStave


traning_sword = SimpleSword('Тренировочный меч', 'Сталь', 10, 5,)
traning_sword_2 = SimpleSword('Тренировочный меч', 'Сталь', 10, 5)
training_bow = SimpleBow('Тренировочный лук', 'обычное дерево', 10, 10, 10)
training_bow_2 = SimpleBow('Тренировочный лук', 'обычное дерево', 10, 10, 10)
training_stave = SimpleStave('Жезл ученика', 'берёза', 10, 10)
training_stave_2 = SimpleStave('Жезл ученика', 'берёза', 10, 10)


list_enemy_training_weapons = [
    traning_sword_2, training_bow_2, training_stave_2
    ]
list_training_weapons = [
    traning_sword, training_bow, training_stave
]
