

try:
    number = float(input('Введите число: '))

except ValueError:
    print('Это не число')
except KeyboardInterrupt:
    print('Ввод с клавиатуры')
except Exception as error:
    print('Произошла ошибка: ', error)
else:
    print(f'Квадрат вашего числа = {number ** 2}')
finally:
    print('Хорошего вам дня <3')