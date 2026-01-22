import random


def is_lucky():
    return random.random() < 0.7


__all__ = ['is_lucky']
