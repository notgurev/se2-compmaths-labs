import math

from Function import Function
from Result import Result
from calculate import dx

import mainboilerplate
from methods.RectanglesMethod import RectanglesMethod
from methods.SimpsonsMethod import SimpsonsMethod
from methods.TrapezoidalMethod import TrapezoidalMethod

methods = {
    1: RectanglesMethod,
    2: TrapezoidalMethod,
    3: SimpsonsMethod
}

predefined_functions = {
    # Решение на Wolfram: https://cutt.ly/UxNbxcL (3.5833)
    1: Function(lambda x: 5 * x ** 3 - 2 * x ** 2 + 3 * x - 15, '5*x^3 - 2*x^2 + 3*x - 15'),
    2: Function(lambda x: math.sin(x) / x, 'sin(x) / x'),
    3: Function(lambda x: 1 / x, '1 / x', True, 0)
}

while True:
    # Выбор функции
    function = mainboilerplate.choose_function(predefined_functions)

    # Выбор метода
    method_number = mainboilerplate.choose_method_number(methods)
    method = methods[method_number]()

    # Ввод исходных данных
    left, right, epsilon, decimal_places = mainboilerplate.read_initial_data()
    if epsilon <= 0:
        print("Точность должна быть больше нуля.")
        continue

    # Решение
    try:
        log('\nПроцесс решения: ')
        if function.symmetrical:
            if abs(left - function.symmetry_point) != abs(right - function.symmetry_point):
                print("Интервал не симметричен, предел не существует.\n")
                continue
            else:
                results_left = method.solve(function, left, function.symmetry_point - dx, epsilon, decimal_places)
                results_right = method.solve(function, function.symmetry_point + dx, right, epsilon, decimal_places)

                results = []
                for result in range(len(results_left)):
                    l = results_left[result]
                    r = results_right[result]
                    results.append(Result(
                        l.integral_value + r.integral_value,
                        max(l.partitions, r.partitions),
                        decimal_places
                    ))
        else:
            results = method.solve(function, left, right, epsilon, decimal_places)
    except TypeError as te:
        print('(!) Ошибка при вычислении значения функции, возможно она не определена на всем интервале.')
        continue

    # Вывод
    print('\n')
    for result in results:
        print(str(result))

    if input('\nЕще раз? [y/n] ') != 'y':
        break
