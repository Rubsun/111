from random import shuffle
from typing import Generator


def custom_shuffle(text: str,  n: int) -> Generator:
    letters = list(text)
    for i in range(n):
        shuffle(letters)
        yield ''.join(letters)

print(*[i for i in custom_shuffle('kshg', 4)])