with open("data/chicken.txt", "r", encoding='UTF-8') as f:
    for line in f:
        data = line.strip().split(": ")
        machul = data[1]
    total_machul = 0
    total_days = 0
    