import random

from brain_games.engine import engine
from brain_games.random import make_random

OPERATORS = ['-', '+', '*']

RULES = 'What is the result of the expression?'


def calc(operator, operand1, operand2):
    if operator == '-':
        return operand1 - operand2
    if operator == '+':
        return operand1 + operand2
    if operator == '*':
        return operand1 * operand2


def make_calc():
    result = []
    i = 0
    while i < 3:
        first_operand = make_random()
        second_operand = make_random()
        operator = random.choice(OPERATORS)
        question = f'{first_operand} {operator} {second_operand}'
        answer = calc(operator, first_operand, second_operand)
        result.append((question, f'{answer}'))
        i += 1
    engine(RULES, result)
