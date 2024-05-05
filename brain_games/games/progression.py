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
        list_of_numbers = list(range(1, 100))
        l_f_k = []
        random_interval_number = random.randint(2, 9)
        interval_number = random_interval_number
        string_of_question = ""
        while len(l_f_k) < 10:
            l_f_k.append(list_of_numbers[interval_number])
            interval_number += random_interval_number
        for i in l_f_k:
            if len(string_of_question) > 1:
                string_of_question += str(i) + ' '
            else:
                string_of_question += ".. "
        print('Question: ' + string_of_question)
        a = prompt.string('Your answer: ')
        if a == str(l_f_k[0]):
            print('Correct!')
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{l_f_k[0]}'.")
            print(f"Let's try again, {name}!")
            return
        tries += 1
    print(f'Congratulations, {name}!')
