with open("data/chicken.txt", "r", encoding='UTF-8') as f:
    total_machul = 0
    days = 0
    for line in f:
        data = line.strip().split(": ")
        machul = int(data[1])
        total_machul += machul
        days += 1
    print(total_machul)
    print(total_machul/days)
    
    