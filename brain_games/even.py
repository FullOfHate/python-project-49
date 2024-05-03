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
        if answer == 'yes':
            if question % 2 == 0:
                print(Fore.GREEN + 'Correct!')
            else:
                print(Fore.RED + f"""'yes' is wrong answer ;(. Correct answer was 'no'. \n Let's try again, {name}""")
                break
        if answer == 'no':
            if question % 2 != 0:
                print(Fore.GREEN + 'Correct!')
            else:
                print(Fore.RED + f"""'no' is wrong answer ;(. Correct answer was 'yes'. \n Let's try again, {name}""")
                break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
