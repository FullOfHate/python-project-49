import prompt
import random
from colorama import Fore


def prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(Fore.YELLOW + 'Answer "yes" if given number is prime. Otherwise answer "no"')
    tries = 0
    while tries < 3:
        random_number = random.randint(1, 100)
        devisor = 1
        list_of_devisor = []
        while devisor <= random_number:
            if random_number % devisor == 0:
                list_of_devisor.append(devisor)
                devisor += 1
            else:
                devisor += 1
        if len(list_of_devisor) > 2:
            result = 'no'
        else:
            result = 'yes'
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        if answer == result:
            print(Fore.GREEN + 'Correct!')
        else:
            print(Fore.RED + f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'. \n Let's try again, {name}!""")
            break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
