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
        random_len = random.randint(5, 10)
        random_start_number = random.randint(1, 10)
        rand_inter_number = random.randint(2, 10)
        random_number_hide = random.randint(1, random_len)
        string_of_question = ""
        while len(list_of_numbers) <= random_len:
            if len(list_of_numbers) == 0:
                list_of_numbers.append(random_start_number)
            else:
                list_of_numbers.append(list_of_numbers[-1] + rand_inter_number)
        for i in list_of_numbers:
            if list_of_numbers.index(i) == random_number_hide:
                string_of_question += ".."
                res = i
                string_of_question += " "
            else:
                string_of_question += str(i) + " "
        print('Question: ' + string_of_question)
        answer = prompt.string('Your answer: ')
        if answer == str(res):
            print(Fore.GREEN + 'Correct!')
            res = 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            return
        tries += 1
    print(f'Congratulations, {name}!')
