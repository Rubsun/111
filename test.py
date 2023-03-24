n = int(input())
answer = 0
temporary = 0
temporary_min = 0
temporary2 = 0

for i in range(n):
    number = int(input())
    # if temporary > number:
    #     temporary_min = number
    # else:
    #     temporary_min = temporary
    temporary_min += min(number, temporary)
    temporary = number
    answer += temporary_min

print(temporary_min)