import math
from Equation import Equation
from methods.ChordMethod import ChordMethod
from methods.NewtonsMethod import NewtonsMethod
from methods.SimpleIterationsMethod import SimpleIterationsMethod

import mainboilerplate

methods = {
    1: ChordMethod,
    2: NewtonsMethod,
    3: SimpleIterationsMethod
}

predefined_functions = {
    # Решение на Wolfram: https://cutt.ly/uzJRsiR
    1: Equation(lambda x: (-2.4 * x ** 3 + 1.27 * x ** 2 + 8.63 * x + 2.31), '−2.4*x^3 + 1.27*x^2 + 8.63*x + 2.31'),
    # https://cutt.ly/6zNbCha
    2: Equation(lambda x: (x / 2 - 2 * (x + 2.39) ** (1 / 3)), 'x/2 - 2*(x + 2.39)^(1/3)'),
    # https://cutt.ly/MzNdHH5
    3: Equation(lambda x: (-x / 2 + math.e ** x + 5 * math.sin(x)), '-x/2 + e^x + 5*sin(x)')
}

ENABLE_LOGGING = True

while True:
    # Выбор функции
    function = mainboilerplate.choose_equation(predefined_functions)

    # Выбор метода
    method_number = mainboilerplate.choose_method_number(methods)

    while True:
        # Ввод исходных данных
        left, right, epsilon, decimal_places = mainboilerplate.read_initial_data()

        # Верификация исходных данных
        method = methods[method_number](function, left, right, epsilon, decimal_places, ENABLE_LOGGING)
        try:
            verified, reason = method.check()
        except TypeError as te:
            print('(!) Ошибка при вычислении значения функции, возможно она не определена на всем интервале.')
            continue
        if verified:
            break
        else:
            print('(!) Введенные исходные данные для метода некорректны: ', reason)

    # Вывод графика функции
    try:
        function.draw(left, right)
    except Exception as e:
        print('(!) Не удалось построить график функции, ', e)

    # Выбор места вывода результата
    output_file_name = input("Введите имя файла для вывода результата или пустую строку, чтобы вывести в консоль: ")

    # Решение
    try:
        if ENABLE_LOGGING:
            print('Процесс решения: ')
        result = method.solve()
    except Exception as e:
        print(e)
        print('(!) Что-то пошло не так при решении: ', e)
        continue

    # Вывод
    mainboilerplate.print_result(result, output_file_name)

    if input('\nЕще раз? [y/n] ') != 'y':
        break
