import random

vocab = {}

# 파일에서 단어장을 생성
with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 단어장에서 무작위로 단어를 선택하여 퀴즈 진행
keys = list(vocab.keys())

while True:  # 무한 루프로 퀴즈를 계속 진행
    random_index = random.randint(0, len(keys) - 1)
    english_word = keys[random_index]
    korean_word = vocab[english_word]

    guess = input("{}: ".format(korean_word))

    if guess == english_word:
        print("맞았습니다!\n")
    if "q" == guess:
        break

    else:   
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
    
    
