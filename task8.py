n = int(input())

temporary = 0 #Временная переменная для сравнения с числом "мусорка"
temporary_min = 0 #Временная переменная для поглучения минимального числа
answer = 0 #Переменная для ответа

for i in range(n):
    number1 = int(input())

    if number1 > temporary: #Начало цикла поиска минимального числа из двух переменных
        temporary_min = temporary
    elif number1 < temporary:
        temporary_min = number1
    elif number1 == temporary:
        temporary_min = temporary#Конец цикла поиска

    temporary = number1 #Передаем старую переменную нашей "мусорке"
    answer += temporary_min #Счетаем сумму минимальных чисел
    
print(answer)

#Столько думал, а оказалось так легко
