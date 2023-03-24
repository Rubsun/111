n = int(input())
list = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']*n
a = 0
b = 0
lsit1 = []

if len(list) == len(list)//n:
    print(list * (len(list)))
elif n <= len(list):
    print(list[:n])
else:
    for i in range(n):
        lsit1.append(list[i])
    print(lsit1)