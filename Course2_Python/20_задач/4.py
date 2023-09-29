from pprint import pprint

data = {i: round(i**0.5, 1) if i >= 0 else 'Ошибка' for i in range(-20, 21)}
pprint(data)
