import random 
rest_number = 4
answer_number = random.randint(1,20)
10
for i in range(rest_number):
    game_number = int(input("기회가 {0} 번 남았습니다. 1 - 20 사이의 숫자를 맞혀 보세요.".format(rest_number - i)))

    if answer_number == game_number:
        print("축하합니다. {0} 만에 숫자를 맞히셨습니다.".format(i + 1))
        break
    elif answer_number > game_number:
        print("Up")
    elif answer_number < game_number:
        print("Down")
if answer_number != game_number:
    print("아쉽습니다. 정답은 {0} 입니다.".format(answer_number))