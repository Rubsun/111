numbers = list(map(int, input()))
dir = input()
way = dir[0].lower()
counter = int(dir[1])


if way == 'f':
    for i in range(counter):
        numbers.insert(0, numbers.pop())
        print(numbers)
elif way == 'b':
    for i in range(counter):
        numbers.insert(-1, numbers.pop(0))
        print(numbers)
# print(numbers)
