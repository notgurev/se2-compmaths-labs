import math

import numpy
from tabulate import tabulate as tab

from plot import *
from boilerplate import *
from methods import *

functions = (
    (lambda t: math.sin(t), 'sin(x)'),
    (lambda t: math.e ** t, 'e^x'),
    (lambda t: t ** 3 + t - 10, 'x^3 + x - 10')
)

methods = (
    (lagrange, 'Многочлен Лагранжа'),
    (newton, 'Многочлен Ньютона с конечными разностями')
)

MAX_POINTS = 20

if __name__ == '__main__':
    while True:
        # набор данных или функция
        if bool_choice('Вы хотите использовать исходные данные на основе функции?'):
            # Функция
            print('Выберите функцию. ')
            print_indexed_list(map(lambda tup: tup[1], functions))
            index = int(number_input('Введите индекс: ', min=1, max=len(functions)))
            func, _ = functions[index - 1]
            left, right = float_interval_choice('Введите интервал: ')
            nodes = int(
                number_input(f'Введите количество узлов интерполяции (2-{MAX_POINTS}): ', min=2, max=MAX_POINTS))

            x = list(numpy.linspace(left, right, nodes))
            y = list(map(lambda t: func(t), x))
            dataset = [x, y]
        else:
            # Таблица
            dataset = read_table()
            left = min(dataset[0])
            right = max(dataset[0])

        print()
        print(tab(dataset, tablefmt='fancy_grid', floatfmt='2.4f'))
        print()

        x0 = number_input('Введите x0: ', min=left, max=right)

        print('\nLets go!\n')

        print('Результаты: ')
        x, y = dataset
        for solve, name in methods:
            try:
                result, table = solve(x, y, x0)
                plot(dataset, x0, result, solve, name)
                print(name + ':', result)
                if table is not None:
                    print(tab(table, tablefmt='fancy_grid', floatfmt='2.2f', headers=['y', *[f'Δ{i}y' for i in range(len(x))]]))
            except Exception as e:
                raise e

        print()
        if input('Еще раз? [y/n] ') != 'y':
            break
