from pprint import pprint
data = {}
for i in range(-20, 21):
    if i >= 0:
        data[i] = round(i **0.5, 2)
    else:
        data[i] = 'Ошибка'
pprint(data)