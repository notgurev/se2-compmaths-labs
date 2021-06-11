from typing import Callable

MIN = 2


def create_dataset(get_line: Callable[..., str]):
    x = list(map(float, get_line().replace(',', '.').split()))
    y = list(map(float, get_line().replace(',', '.').split()))
    if len(x) != len(y) or len(x) <= MIN:
        print(f"Введите корректную таблицу, содержащую не менее {MIN} точек.")
        return None
    return [x, y]


def read_initial_data():
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        try:
            input_function = input if filename == '' else open(filename, "r").readline
            dataset = create_dataset(input_function)
            if dataset is not None:
                return dataset
        except FileNotFoundError:
            print('Файл не найден.')
        except:
            print('Что-то пошло не так.')
