import prompt
import random
from colorama import Fore


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries = 0
    while tries < 3:
        question = random.randint(0, 100)
        print(Fore.YELLOW + 'Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            c_a = 'yes'
        else:
            c_a = 'no'
        wr_an_1 = f"'{answer}' is wrong answer ;(. Correct answer was '{c_a}'."
        wr_an_2 = f"Let's try again, {name}!"
        if answer == 'yes':
            if question % 2 == 0:
                print(Fore.GREEN + 'Correct!')
            else:
                print(wr_an_1)
                print(wr_an_2)
                return
        elif answer == 'no':
            if question % 2 != 0:
                print('Correct!')
            else:
                print(wr_an_1)
                print(wr_an_2)
                return
        else:
            print(wr_an_1)
            print(wr_an_2)
            return
        tries += 1
    print(f'Congratulations, {name}!')
