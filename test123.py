temp1 = 0
inp = 0
count1 = 0 #Счетчик монотонности на убывание
count2 = 0 #Счетчик монотонности на возрастание
answer = 0 #Итоговый ответ

while True:
    inp = int(input())
    if inp == 0: #Если последовательность началась с нуля или он появился позже
        break
    elif temp1 == inp:
        count1 = 1
        count2 = 1
    elif temp1 > inp:
        count1 += 1
        count2 = 1
        if count1 > answer:
            answer = count1
    elif temp1 < inp:
        count2 += 1
        count1 = 1
        if count2 > answer:
            answer = count2
    temp1 = inp


print(answer)

