from math import sin, cos, exp

import plot
from boilerplate import *
from methods import *

func1 = (
    lambda x, y: math.sin(x) + y,
    "y' = sin(x) + y",
    lambda x0, y0: (y0 + sin(x0) / 2 + cos(x0) / 2) / exp(x0),  # C calculator
    lambda c, x: c * exp(x) - sin(x) / 2 - cos(x) / 2  # Exact Solution
)

func2 = (
    lambda x, y: y * x,
    "y' = y * x",
    lambda x0, y0: y0 / exp((x0 ** 2) / 2),
    lambda c, x: c * exp((x ** 2) / 2)
)

functions = (
    func1,
    func2
)

methods = (
    (euler, 'Метод Эйлера', 1),
    # (milne, 'Метод Милна', 4),
    (adams, 'Метод Адамса', 4),
)


class CompException(Exception):
    pass


if __name__ == '__main__':
    while True:
        # Функция
        print('Выберите функцию. ')
        print_indexed_list([tup[1] for tup in functions])
        index = int(number_input('Введите индекс: ', min=1, max=len(functions)))
        func, _, calculate_c, func_exact = functions[index - 1]
        left, right = float_interval_choice('Введите интервал: ')
        y0 = float(number_input(f'Введите начальное условие y({left}): '))
        h = float(number_input('Введите шаг: ', min=0.00001))
        eps = float(number_input('Введите точность: ', min=0.00001))

        print('\nLets go!\n')

        print('Результаты: ')
        for solve, name, p in methods:
            try:
                print('~', name, '~\n')
                c = calculate_c(left, y0)
                exact = lambda x: func_exact(c, x)
                X, Y, output = solve(func, left, right, y0, h, exact, eps)
                print(output)

                # Решить с 2h
                X2h, Y2h, _ = solve(func, left, right, y0, 2 * h, exact, eps)
                R = (Y[2] - Y2h[2]) / (2 ** p - 1)
                print(f'Оценка точности по правилу Рунге: R = {R}')

                plot.plot([X, Y], name, exact)
            except CompException as e:
                print(e)

        print()
        if input('Еще раз? [y/n] ') != 'y':
            break
