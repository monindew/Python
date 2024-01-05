with open ("vocabulary.txt", "r", encoding="UTF-8") as f:
    for line in f:
        data = line.strip().split(": ")
        englist_word, korean_word = data[0], data[1]
     
        guess = input("{}: ".format(korean_word))

        if guess == englist_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(englist_word))
   
    