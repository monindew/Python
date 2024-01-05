from random import randint


def generate_numbers(n):
    choose_number = []
    while len(choose_number) < n:
            num = randint(1,45)
            if num not in choose_number:
                  choose_number.append(num)
    return choose_number


