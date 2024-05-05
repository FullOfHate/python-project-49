import prompt
import random
from colorama import Fore


def gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(Fore.YELLOW + 'Find the greatest common divisor of given numbers.')
    result = 1      # запоминаем делитель
    devisor_2_check = 1     # проверяем делитель
    tries = 0
    while tries < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        counter_end = min(num_1, num_2)     # останавливаем перебор на этом числе
        counter_start = 0                   # начинаем перебор с этого числа
        while counter_start <= counter_end:
            if num_1 % devisor_2_check == 0 and num_2 % devisor_2_check == 0:
                result = devisor_2_check
                devisor_2_check += 1
                counter_start += 1
            else:
                counter_start += 1
                devisor_2_check += 1
        print('Question: {num_1} {num_2}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print(Fore.GREEN + 'Correct!')
            result = 1
            devisor_2_check = 1
        else:
            print(Fore.RED + f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'. \n Let's try again, {name}""")
            break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
