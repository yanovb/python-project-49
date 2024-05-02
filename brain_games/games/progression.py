import random

from brain_games.engine import engine
from brain_games.random import make_random, make_step, make_length_progression

RULES = 'What number is missing in the progression?'


def make_question(first_number, step, length):
    result = []
    number = first_number
    i = 0
    while i < length:
        number += step
        result.append(f'{number}')
        i += 1
    answer = random.choice(result)
    result[result.index(answer)] = '..'
    question = ' '.join(result)
    return [question, answer]


def make_progression():
    result = []
    i = 0
    while i < 3:
        number = make_random()
        step = make_step()
        length = make_length_progression()
        [question, answer] = make_question(number, step, length)
        result.append((question, answer))
        i += 1
    engine(RULES, result)
