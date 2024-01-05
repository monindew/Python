from random import randint


def generate_numbers(n):
    choose_number = []
    while len(choose_number) < n:
            num = randint(1,45)
            if num not in choose_number:
                  choose_number.append(num)
    return choose_number


def draw_winning_numbers():
    random_winning_numbers = generate_numbers(6)
    random_winning_numbers.sort()
    while True:
        bonus_number = randint(1,45)
        if bonus_number not in random_winning_numbers:
            random_winning_numbers.append(bonus_number)
            break
    return random_winning_numbers

def count_matching_numbers(numbers, winning_numbers):
    i = 0
    for num in numbers :
        if numbers in winning_numbers[:6]:
            i += 1
    return i

def check(numbers, winning_numbers):
    i = count_matching_numbers(numbers, winning_numbers)
    if i == 6:
        return 1000000000
    if i == 5:
        if winning_numbers[6] in numbers:
            return 50000000
        else:
            return 1000000
    if i == 4:
        return 50000
    if i == 3:
        return 5000
    if i <= 2:
        return 0