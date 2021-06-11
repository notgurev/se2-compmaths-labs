from tabulate import tabulate
from termcolor import cprint


# Метод Гаусса
def solve_matrix(input_matrix):
    check_square_matrix(input_matrix)
    length_of_matrix = len(input_matrix)
    do_triangle_matrix(input_matrix)
    is_singular(input_matrix)
    input_answer_matrix = [0 for i in range(length_of_matrix)]
    for k in range(length_of_matrix - 1, -1, -1):
        input_answer_matrix[k] = (input_matrix[k][-1] - sum(
            [input_matrix[k][j] * input_answer_matrix[j] for j in range(k + 1, length_of_matrix)])) / input_matrix[k][k]
    return input_answer_matrix


# Checking the matrix
def check_square_matrix(input_matrix):
    for i in range(len(input_matrix)):
        if len(input_matrix) + 1 != len(input_matrix[i]):
            raise Exception('ERROR: The size of matrix isn\'t correct')
        count = 0
        for j in range(len(input_matrix[i]) - 1):
            if input_matrix[i][j] == 0:
                count += 1
        if count == len(input_matrix[i]) - 1:
            raise Exception('ERROR: The matrix has no solutions')


def do_triangle_matrix(input_matrix):
    length_of_matrix = len(input_matrix)  # = number of rows
    for k in range(length_of_matrix - 1):
        get_max_element_in_column(input_matrix, k)
        for i in range(k + 1, length_of_matrix):
            div = input_matrix[i][k] / input_matrix[k][k]
            input_matrix[i][-1] -= div * input_matrix[k][-1]
            for j in range(k, length_of_matrix):
                input_matrix[i][j] -= div * input_matrix[k][j]
    return length_of_matrix


class SingularMatrixException(Exception):
    pass


# Проверка на вырожденность матрицы
def is_singular(input_matrix):
    if count_determinant_for_square_matrix(input_matrix) == 0:
        raise SingularMatrixException('Ошибка: вырожденная матрица')


# Поиск главного элемента в столбце
def get_max_element_in_column(input_matrix, number_of_column):
    max_element = input_matrix[number_of_column][number_of_column]
    max_row = number_of_column
    for j in range(number_of_column + 1, len(input_matrix)):
        if abs(input_matrix[j][number_of_column]) > abs(max_element):
            max_element = input_matrix[j][number_of_column]
            max_row = j
    if max_row != number_of_column:
        input_matrix[number_of_column], input_matrix[max_row] = input_matrix[max_row], input_matrix[number_of_column]
    return input_matrix


# Печать матрицы
def print_matrix(input_matrix, decimals):
    cprint(tabulate(input_matrix, tablefmt="fancy_grid", floatfmt=f"2.{decimals}f"))


# Вектор невязок
def do_residual_vector(input_matrix, input_answer_matrix):
    big_matrix = []
    little_matrix = []
    for i in range(len(input_matrix)):
        big_matrix.append(input_matrix[i][0:len(input_matrix)])
        little_matrix.append(input_matrix[i][len(input_matrix):])
    x_matrix = input_answer_matrix
    temp = [0] * len(input_matrix)
    residual_vector = [0 for i in range(len(input_matrix))]
    for i in range(len(big_matrix)):
        temp[i] = 0
        for j in range(len(big_matrix)):
            temp[i] += x_matrix[j] * big_matrix[i][j]
        residual_vector[i] = temp[i] - little_matrix[i][0]


# Определитель матрицы
def count_determinant_for_square_matrix(input_matrix):
    determinant = 1
    for i in range(len(input_matrix)):
        determinant *= input_matrix[i][i]
    return round(determinant, 5)
