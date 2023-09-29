from typing import Generator
def countup(n:int) -> Generator:
    # for i in range(0, abs(n)+1, 2):
    #     yield i if n>= 0 else -1
    step = 1 if n>= 0 else -1
    for i in range(0, n+1,2*step):
        yield i

# print(list(countup(10)))
# Способы вывода
# for i in countup(6):
    # print(i)