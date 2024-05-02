from brain_games.engine import engine
from brain_games.random import make_random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    result = 'yes' if number % 2 == 0 else 'no'
    return result


def make_even():
    result = []
    i = 0
    while i < 3:
        question = make_random()
        answer = is_even(question)
        result.append((question, answer))
        i += 1
    engine(RULES, result)
