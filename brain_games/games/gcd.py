import math

from brain_games.engine import engine
from brain_games.random import make_random


RULES = 'Find the greatest common divisor of given numbers.'


def make_gcd():
    result = []
    i = 0
    while i < 3:
        first_number = make_random()
        second_number = make_random()
        question = f'{first_number} {second_number}'
        answer = math.gcd(first_number, second_number)
        result.append((question, f'{answer}'))
        i += 1
    engine(RULES, result)
