import prompt
import random
from colorama import Fore


def gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(Fore.YELLOW + 'Find the greatest common divisor of given numbers.')
    res = 1      # запоминаем делитель
    devisor_2_check = 1     # проверяем делитель
    tries = 0
    while tries < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        counter_end = min(num_1, num_2)
        counter_start = 0
        while counter_start <= counter_end:
            if num_1 % devisor_2_check == 0 and num_2 % devisor_2_check == 0:
                res = devisor_2_check
                devisor_2_check += 1
                counter_start += 1
            else:
                counter_start += 1
                devisor_2_check += 1
        print(f'Question: {num_1} {num_2}')
        answer = prompt.string('Your answer: ')
        if answer == str(res):
            print(Fore.GREEN + 'Correct!')
            res = 1
            devisor_2_check = 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print("Let's try again, {name}!")
            break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
