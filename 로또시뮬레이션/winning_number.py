from choose_number import generate_numbers
from random import randint


def draw_winning_numbers():
    random_winning_numbers = generate_numbers(6)
    random_winning_numbers.sort()
    while True:
        bonus_number = randint(1,45)
        if bonus_number not in random_winning_numbers:
            random_winning_numbers.append(bonus_number)
            break
    return random_winning_numbers

print(draw_winning_numbers())
