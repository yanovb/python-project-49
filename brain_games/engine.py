import prompt


def engine(rules, qs_and_as):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    for q_a in qs_and_as:
        print(f'Question: {q_a[0]}')
        ua = prompt.string('Your answer: ')
        if ua != q_a[1]:
            print(f'"{ua}" is wrong answer ;(. Correct answer was "{q_a[1]}".')
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
