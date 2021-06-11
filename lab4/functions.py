import math
from functools import reduce
from typing import List, Callable

from matrix import solve_matrix, SingularMatrixException

UNSOLVABLE = (None, math.inf, None)


def calculate_S(values_first: List[float], values_second: List[float]) -> float:
    """S - мера отклонения, критерий минимизации"""
    s = 0
    for first, second in list(zip(values_first, values_second)):
        s += (first - second) ** 2
    return s


def calculate_deviation(s: float, n: float) -> float:
    """δ - среднеквадратичное отклонение"""
    return math.sqrt(s / n)


def calc_deviations(f: Callable, x, y):
    s = calculate_S([f(_x) for _x in x], y)
    print('Мера отклонения:', s)

    delta = calculate_deviation(s, len(y))
    print('Среднеквадратичное отклонение:', delta)
    return s, delta


# -----------------------------------------------------

def linear(x, y):
    sx, sxx, sy, sxy = [0] * 4
    for i in range(len(x)):
        sx += x[i]
        sxx += x[i] ** 2
        sy += y[i]
        sxy += x[i] * y[i]
    a, b = solve_matrix([[sxx, sx, sxy], [sx, len(x), sy]])
    function_text = f'Линейная аппроксимация: y = {a:.4f} * x + {b:.4f}'
    print(function_text)

    func = lambda _x: a * _x + b
    _, delta = calc_deviations(func, x, y)

    # Коэффициент Пирсона
    average_x = sum(x) / len(x)
    average_y = sum(y) / len(y)

    numerator = sum([(x[i] - average_x) * (y[i] - average_y) for i in range(len(x))])

    sum_sq_x = reduce(lambda prev, curr: prev + (curr - average_x) ** 2, x, 0)
    sum_sq_y = reduce(lambda prev, curr: prev + (curr - average_y) ** 2, y, 0)

    denominator = math.sqrt(sum_sq_x * sum_sq_y)

    r = numerator / denominator
    print('Коэффициент Пирсона:', r)

    return function_text, delta, func


def quadratic(x, y):
    sx, sx2, sx3, sx4, sy, sxy, sx2y = [0] * 7
    for i in range(len(x)):
        sx += x[i]
        sx2 += x[i] ** 2
        sx3 += x[i] ** 3
        sx4 += x[i] ** 4
        sy += y[i]
        sxy += x[i] * y[i]
        sx2y += x[i] ** 2 * y[i]
    try:
        c, b, a = solve_matrix([[len(x), sx, sx2, sy], [sx, sx2, sx3, sxy], [sx2, sx3, sx4, sx2y]])
    except SingularMatrixException:
        print('Квадратичная аппроксимация невозможна.')
        return UNSOLVABLE
    function_text = f'Квадратичная аппроксимация: y = {a:.4f} * x^2 + {b:.4f} * x + {c:.4f}'
    print(function_text)

    func = lambda _x: a * _x ** 2 + b * _x + c
    _, delta = calc_deviations(func, x, y)

    return function_text, delta, func


def exponent(x, y):
    sx, sxx, sy, sxy = [0] * 4
    for i in range(len(x)):
        if y[i] > 0:
            sx += x[i]
            sxx += x[i] ** 2
            sy += math.log(y[i], math.e)
            sxy += x[i] * math.log(y[i], math.e)
        else:
            print('Экспоненциальная аппроксимация невозможна.')
            return UNSOLVABLE
    a, b = solve_matrix([[len(x), sx, sy], [sx, sxx, sxy]])
    a = math.e ** a
    function_text = f'Экспоненциальная аппроксимация: y = {a:.4f} * e^({b:.4f} * x)'
    print(function_text)

    func = lambda _x: a * (math.e ** (b * _x))
    _, delta = calc_deviations(func, x, y)

    return function_text, delta, func


def logarithmic(x, y):
    sx, sxx, sy, sxy = [0] * 4
    for i in range(len(x)):
        if x[i] > 0:
            sx += math.log(x[i], math.e)
            sxx += math.log(x[i], math.e) ** 2
            sy += y[i]
            sxy += math.log(x[i], math.e) * y[i]
        else:
            print('Логарифмическая аппроксимация невозможна.')
            return UNSOLVABLE
    b, a = solve_matrix([[len(x), sx, sy], [sx, sxx, sxy]])
    function_text = f'Логарифмическая аппроксимация: y = {a:.4f} * ln(x) + {b:.4f}'
    print(function_text)

    func = lambda _x: a * math.log(_x, math.e) + b
    _, delta = calc_deviations(func, x, y)

    return function_text, delta, func


def power(x, y):
    sx, sxx, sy, sxy = [0] * 4
    for i in range(len(x)):
        if y[i] > 0 and x[i] > 0:
            sx += math.log(x[i], math.e)
            sxx += math.log(x[i], math.e) ** 2
            sy += math.log(y[i], math.e)
            sxy += math.log(x[i], math.e) * math.log(y[i], math.e)
        else:
            print('Степенная аппроксимация невозможна.')
            return UNSOLVABLE
    a, b = solve_matrix([[len(x), sx, sy], [sx, sxx, sxy]])
    a = math.e ** a
    function_text = f'Степенная аппроксимация: y = {a:.4f} * x^{b:.4f}'
    print(function_text)

    func = lambda _x: a * _x ** b
    _, delta = calc_deviations(func, x, y)

    return function_text, delta, func
