from interface_game.main_menu import (InfoHeroPage, InfoWeaponsHeroPage,
                                      MainMenuPage, TrainingMenuPage)
from interface_game.trainings.chose_enemy import (TrainingEnemyClose,
                                                  TrainingEnemyMagic,
                                                  TrainingEnemyMenu,
                                                  TrainingEnemyRanged)
from interface_game.trainings.chose_weapon_enemy_close import (
    TrainingWeaponCloseEnemyClose, TrainingWeaponMagicEnemyClose,
    TrainingWeaponRangedEnemyClose, WeaponHeroPageEnemyClose)
from interface_game.trainings.chose_weapon_enemy_magic import (
    TrainingWeaponCloseEnemyMagic, TrainingWeaponMagicEnemyMagic,
    TrainingWeaponRangedEnemyMagic, WeaponHeroPageEnemyMagic)
from interface_game.trainings.chose_weapon_enemy_ranged import (
    TrainingWeaponCloseEnemyRanged, TrainingWeaponMagicEnemyRanged,
    TrainingWeaponRangedEnemyRanged, WeaponHeroPageEnemyRanged)

pages = (
    MainMenuPage, TrainingMenuPage, TrainingEnemyMenu, TrainingEnemyClose,
    TrainingEnemyRanged, TrainingEnemyMagic, InfoHeroPage, InfoWeaponsHeroPage,
    TrainingWeaponCloseEnemyClose, WeaponHeroPageEnemyClose,
    TrainingWeaponRangedEnemyClose, TrainingWeaponMagicEnemyClose,
    TrainingWeaponCloseEnemyRanged, TrainingWeaponMagicEnemyRanged,
    TrainingWeaponRangedEnemyRanged, WeaponHeroPageEnemyRanged,
    TrainingWeaponCloseEnemyMagic, TrainingWeaponMagicEnemyMagic,
    TrainingWeaponRangedEnemyMagic, WeaponHeroPageEnemyMagic
)