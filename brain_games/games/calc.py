import prompt
import random
from colorama import Fore


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(Fore.YELLOW + 'What is the result of the expression?')
    list_of_signs = ['+', '-', '*']
    tries = 0
    while tries < 3:
        num_1 = random.randint(0, 10)
        num_2 = random.randint(0, 10)
        sign = random.choice(list_of_signs)
        print(Fore.YELLOW + ('Question: ' + str(num_1) + " " + sign + " " + str(num_2)))
        if sign == '+':
            result = num_1 + num_2
        elif sign == '-':
            result = num_1 - num_2
        else:
            result = num_1 * num_2
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print(Fore.GREEN + 'Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
