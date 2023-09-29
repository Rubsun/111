
#Если нам гарантируют что выражение правельно записано, то если мы встречаем вычеслительный знак гарантируется что перед ним будет два числа. По этой логике все и работает. Когда мы что то вычеслили мы это удаляяем.

string = input().split()
answer = 0
i = 0
while len(string) > 1:
    for i in range(len(string)):
        if string[i] == '+':
            answer = int(string[i-2]) + int(string[i-1])
            string[i] = str(answer)
            string.pop(i-1)
            string.pop(i-2)
            print(string)
            break
        elif string[i] == '-':
            answer = int(string[i-2]) - int(string[i-1])
            string[i] = str(answer)
            string.pop(i-1)
            string.pop(i-2)
            print(string)
            break
        elif string[i] == '*':
            answer = int(string[i-2]) * int(string[i-1])
            string[i] = str(answer)
            string.pop(i-1)
            string.pop(i-2)
            print(string)
            break
print(answer)
