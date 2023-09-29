from random import sample
from typing import Iterable


def random_procent(data: Iterable, n: int = 1) -> tuple:
    if n > len(data):
        n = len(data)
    chooses_numbers = sample(data, n)
    print(f'{ chooses_numbers, (n /  len(data)) * 100 }%')



random_procent([1, 2, 3, 4])
