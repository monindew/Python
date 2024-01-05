with open("vocabulary.txt", "a", encoding="UTF-8") as f:
    while True:
        eng_input = input("영어 단어를 입력하세요: ")
        if eng_input == 'q':
            break

        kor_input = input("한글 단어를 입력하세요: ")
        if kor_input == 'q':
            break

        f.write("{0}: {1} \n".format(eng_input,kor_input))
