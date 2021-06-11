from matrix import Matrix
from solve import solve


def create_filled_matrix(size: int, get_line) -> Matrix:
    data = []
    right = []
    for line in range(0, size):
        equation = list(map(float, get_line().split()))
        right.append(equation.pop())
        data.append(equation)
    return Matrix(size, data, right)


def validate_size(size: int):
    if not 0 < size <= 20:
        print('Матрица должна иметь размер от 1 до 20 включительно.')
        exit(-1)
    return size


while True:
    filename = input("Введите имя файла для загрузки матрицы или пустую строку, чтобы ввести вручную: ")

    if filename == '':
        precision = input('Точность: ')
        size = validate_size(int(input('Размер матрицы: ')))
        print('Коэффициенты матрицы: ')
        matrix = create_filled_matrix(size, input)
    else:
        try:
            f = open(filename, "r")
            precision = f.readline()
            size = validate_size(int(f.readline()))
            matrix = create_filled_matrix(size, f.readline)
            f.close()
        except FileNotFoundError:
            print('Файл не найден.')
            continue

    print('Исходная матрица:')
    print(matrix)

    solution = solve(matrix, precision)

    if solution:
        print('\nРешение:')
        print(solution)

    if input('Еще раз? [y/n] ') != 'y':
        break
