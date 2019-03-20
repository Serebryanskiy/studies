import numpy as np


def ifeellucky():
    result = np.random.uniform(0, 1)  # от 0 включая до 1 не включая
    monte = int(result * 37)  # округляет вниз, 37 не может быть

    if monte < 1:
        print(f'Выпало {monte} Зеро')
    elif monte % 2 == 0:
        print(f'Выпало {monte} чёрное')
    else:
        print(f'Выпало {monte} красное')

    answer = input('Делайте Ваши ставки! (Y/n)')
    if answer == 'y' or answer == 'Y':
        ifeellucky()
    else:
        print('Спасибо за игру!')


ifeellucky()

np.var