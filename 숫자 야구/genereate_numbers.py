from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        gen_number = randint(0,9)
        if gen_number not in numbers:
            numbers.append(gen_number)
            
    # 여기에 코드를 작성하세요

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 테스트 코드
print(generate_numbers())