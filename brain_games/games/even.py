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
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        wrong_answer = f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. \n Let's try again, {name}!"""
        if answer == 'yes':
            if question % 2 == 0:
                print(Fore.GREEN + 'Correct!')
            else:
                print(Fore.RED + wrong_answer)
                break
        elif answer == 'no':
            if question % 2 != 0:
                print(Fore.GREEN + 'Correct!')
            else:
                print(Fore.RED + wrong_answer)
                break
        else:
            print(Fore.RED + wrong_answer)
            break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
