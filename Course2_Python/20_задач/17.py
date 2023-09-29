from time import time
from random import shuffle
from typing import Generator
from typing import Callable


def search_time(func: Callable) -> Callable:
    def new(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print((f'Время: {time()-start}'))
        return result
    return new

@search_time
def custom_shuffle(text: str,  n: int) -> Generator:
    letters = list(text)
    for i in range(n):
        shuffle(letters)
        yield ''.join(letters)


print(*[i for i in custom_shuffle('kshg', 4)])
