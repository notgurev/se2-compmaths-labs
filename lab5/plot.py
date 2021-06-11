import matplotlib.pyplot as plt
import numpy as np


def plot(data, x0, y0, interpolate, title: str):
    data_x, data_y = data
    plt.title = title
    plt.grid(True)

    # Точки
    plt.scatter(data_x, data_y, s=20, label='Исходные данные', zorder=10, color='black')

    # Вычисление Y для полинома
    x_linspace = np.linspace(min(data_x), max(data_x), 100)
    interpolated_y = [interpolate(data_x, data_y, x)[0] for x in x_linspace]

    # Функция
    # v = numpy.vectorize(func)(x_linspace)
    # plt.plot(x_linspace, v, 'green', label='Исходная функция')

    # Полином
    cstl = title.replace('с конечными разностями', '').strip()  # костыль
    plt.plot(x_linspace, interpolated_y, 'blue', zorder=5, label=cstl)

    # Та самая точка
    plt.plot(x0, y0, 'o', color='red', markersize=5, zorder=10, label='Искомое значение')

    # ---
    plt.legend(loc='upper left', fontsize='medium')
    plt.savefig(f'{title}.png')
    plt.show()
