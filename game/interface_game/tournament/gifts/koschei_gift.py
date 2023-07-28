from database.db import return_hero_id, update_hero


def koschei_tournament_gift(hero, max_health_hero):
    """Подарок кощея."""
    hero_id = return_hero_id(hero.name)
    hero.koschei = 1
    values = (max_health_hero, hero.force,
              hero.dexterity, hero.magic, hero.speed,
              hero.protection, hero.experience, hero.tsar,
              hero.teutonic, hero.polovistan, hero.rome,
              hero.persia, hero.barbarians, hero.koschei, hero_id)
    update_hero(values)
