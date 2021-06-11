import matplotlib.pyplot as plt
import numpy as np


def plot(data, title: str, func_exact):
    data_x, data_y = data
    plt.title = title
    plt.grid(True)

    x_exact = np.linspace(min(data_x), max(data_x), 100)
    y_exact = [func_exact(x) for x in x_exact]
    plt.plot(x_exact, y_exact, color='black', label='y = f(x)')

    plt.scatter(data_x, data_y, zorder=10)
    plt.plot(data_x, data_y, zorder=5, label=f'{title}: y ~ f(x)')

    # ---
    plt.legend(loc='upper left', fontsize='medium')
    plt.savefig(f'{title}.png')
    plt.show()
