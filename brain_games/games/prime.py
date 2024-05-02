from brain_games.engine import engine
from brain_games.random import make_random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return 'no'
    return 'yes'


def make_prime():
    result = []
    i = 0
    while i < 3:
        number = make_random()
        question = f'{number}'
        answer = is_prime(number)
        result.append((question, answer))
        i += 1
    engine(RULES, result)
