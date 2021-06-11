import math
from functools import lru_cache
from typing import List

import tabulate

from plot import plot


def lagrange(x, y, x0):
    result = 0
    for j in range(len(y)):
        mul = 1
        for i in range(len(x)):
            if i != j:
                mul *= (x0 - x[i]) / (x[j] - x[i])
        result += y[j] * mul
    return result, None


def check_equidistant_nodes(nodes):
    h = nodes[1] - nodes[0]
    for i in range(len(nodes) - 1):
        if not math.isclose(nodes[i + 1] - nodes[i], h):
            return False
    return True


# Кэш
# precalculated_finite_diffs = None


def newton(x: list[float], y: List[float], interp_x: float):
    # Многочлен Ньютона с конечными разностями

    if not check_equidistant_nodes(x):
        raise Exception('Узлы не являются равноотстоящими, метод Ньютона с конечными разностями не применим.')

    h = x[1] - x[0]

    forward = True

    middle = sum(x) / len(x)
    if interp_x > middle:
        forward = False

    # print(f'Интерполируем: {"вперед" if forward else "назад"}')

    # Выбрать x
    x_for_t, x_for_t_index = None, None
    for i in range(len(x)):
        if interp_x >= x[i]:
            x_for_t_index = i
            x_for_t = x[i]
    #
    # if not forward:
    #     x_for_t_index += 1
    #     x_for_t = x[x_for_t_index]

    n = len(x) - x_for_t_index + 1
    table = [[None for t in range(len(x))] for t in range(len(x))]

    @lru_cache(maxsize=None)
    def calc_finite_difference(level: int, i: int) -> float:
        # print(f'level = {level}, i = {i}')
        if level == 0:
            res = y[i]
            table[i][level] = res
            return res
        else:
            res = calc_finite_difference(level - 1, i + 1) - calc_finite_difference(level - 1, i)
            table[i][level] = res
            return res

    t = ((interp_x - x_for_t) / h) if forward else (interp_x - x[-1]) / h

    def calc_t_stuff(i: int) -> float:
        if i == 0:
            return 1
        else:
            t_mul = 1
            for j in range(i):
                t_mul *= (t - j) if forward else (t + j)
            t_mul /= math.factorial(i)
            return t_mul

    result = 0
    # print(f'x_for_t_index = {x_for_t_index}')

    for i in (range(0, len(x) - x_for_t_index, 1) if forward else range(0, len(x), 1)):
        # print(i)
        if forward:
            result += calc_finite_difference(level=i, i=x_for_t_index) * calc_t_stuff(i)
        else:
            result += calc_finite_difference(level=i, i=len(x) - i - 1) * calc_t_stuff(i)

    return result, table


if __name__ == '__main__':
    x = [0.1, 0.2, 0.3, 0.4, 0.5]
    y = [1.25, 2.38, 3.79, 5.44, 7.14]

    result, table = newton(x, y, 0.35)
    print('ответ', result)
    plot([x, y], 0.45, result, newton, 'aaaaaa')
    print(tabulate.tabulate(table, tablefmt='fancy_grid', floatfmt='.2f'))
