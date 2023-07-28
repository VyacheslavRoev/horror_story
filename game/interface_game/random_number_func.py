from random import randint


def random_phrase(lst):
    phrase = lst[randint(0, len(lst) - 1)]
    return phrase
