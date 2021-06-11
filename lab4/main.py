import matplotlib.pyplot as plt
import numpy as np

import main_boilerplate
from functions import *

solvers = (
    linear,
    quadratic,
    logarithmic,
    exponent,
    power
)

COLORS_CONST = [
    'blue',
    'red',
    'green',
    'black',
    'orange'
]


def draw(approximations: List, data):
    colors = COLORS_CONST.copy()
    data_x, data_y = data
    plt.title = 'Графики полученных эмпирических функций'
    plt.grid(True, which='both')
    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.axhline(y=0, color='gray', label='y = 0')
    # ---

    plt.scatter(data_x, data_y, s=20, zorder=10)

    for i in range(len(approximations)):
        text, _, f = approximations[i]
        # мегакостыль
        text = text.split(':')[0][:4].replace('Лине', 'Лин').replace('Лога', 'Лог')
        x = np.linspace(min(data_x), max(data_x), 100)
        func = np.vectorize(f)(x)

        plt.plot(x, func, colors.pop(), label=text, zorder=5)

    # ---
    plt.legend(loc='upper left', fontsize='medium', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig('graph.png')
    plt.show()


def newline_wrapper(solver, x, y):
    print()
    return solver(x, y)


def solve(data: List[int]):
    x, y = data
    approximations = [newline_wrapper(solver, x, y) for solver in solvers]
    best = approximations[0]
    for approximation in approximations:
        function_text, s, _ = approximation
        _, best_delta, _ = best
        if s < best_delta:
            best = approximation
    filtered = list(filter(lambda approx: approx[1] != math.inf, approximations))
    draw(filtered, data)
    print('\n\t* * *\n')
    print('Наилучшее приближение:')
    print(best[0])
    print(f'СКО = {best_delta}')
    print('\n\t* * *')
    return data


if __name__ == '__main__':
    while True:
        dataset = main_boilerplate.read_initial_data()
        solve(dataset)
        print()
        if input('Еще раз? [y/n] ') != 'y':
            break
