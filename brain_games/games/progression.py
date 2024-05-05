import prompt
import random
from colorama import Fore


def progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(Fore.YELLOW + 'What number is missing in the progression?')
    tries = 0
    while tries < 3:
        list_of_numbers = []
        random_len = random.randint(5, 10)                      # длина списка
        random_start_number = random.randint(1, 10)             # начало списка с этого числа
        random_interval_number = random.randint(2, 10)          # интервал между числами
        random_number_hide = random.randint(1, random_len)         # индекс числа, которое будет скрыто
        string_of_question = ""
        while len(list_of_numbers) <= random_len:
            if len(list_of_numbers) == 0:
                list_of_numbers.append(random_start_number)
            else:
                list_of_numbers.append(list_of_numbers[-1] + random_interval_number)
        for i in list_of_numbers:
            if list_of_numbers.index(i) == random_number_hide:
                string_of_question += ".. "
                result = i
            else:
                string_of_question += str(i) + " "
        print(string_of_question)
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print(Fore.GREEN + 'Correct!')
            result = 1

        else:
            print(Fore.RED + f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'. \n Let's try again, {name}""")
            break
        tries += 1
    if tries == 3:
        print(f'Congratulations, {name}!')
