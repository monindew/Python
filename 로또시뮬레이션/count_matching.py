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