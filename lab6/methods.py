def str_result(i, x, y, f, factual) -> str:
    res = '\n'
    res += f"i: {i}\n"
    res += f"X: {x}\n"
    res += f"Y: {y}\n"
    res += f"F(x, y): {f}\n"
    res += f"Точное значение: {factual}\n"
    return res


def euler(func_tup, left, right, y0, h, exact, eps=None):
    output = ""
    X, Y = [left], [y0]

    i = 0
    while X[i] + h <= right:
        X.append(X[i] + h)
        prev = i
        func_value = func_tup(X[prev], Y[prev])
        y_next = Y[prev] + h * func_value
        Y.append(y_next)

        output += str_result(i, X[i], y_next, func_value, exact(X[i]))

        i += 1
    return X, Y, output


def runge_kutta_4th_order(func, left, right, y0, h, exact, eps=None):
    output = ''
    X, Y = [left], [y0]

    i = 0
    while X[i] + h <= right:
        X.append(X[i] + h)
        prev = i

        k1 = h * func(X[prev], Y[prev])
        k2 = h * func(X[prev] + h / 2, Y[prev] + k1 / 2)
        k3 = h * func(X[prev] + h / 2, Y[prev] + k2 / 2)
        k4 = h * func(X[prev] + h, Y[prev] + k3)

        y_next = Y[prev] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        output += str_result(i, X[i], y_next, func(X[prev], Y[prev]), exact(X[i]))

        Y.append(y_next)
        i += 1
    return X, Y, output


def milne(func, a, b, y0, h, exact, eps):
    output = ""
    X, Y, out = runge_kutta_4th_order(func, a, a + 3.5 * h, y0, h, exact)
    output += out
    x = X[-1] + h
    f = []
    for i in range(1, 4):
        f.append(func(X[i], Y[i]))
    i = 4
    while x <= b:
        X.append(x)

        y_predicted = Y[-4] + 4 * h * (2 * f[0] - f[1] + 2 * f[2]) / 3
        new_f = func(x, y_predicted)
        y_corrected = Y[-2] + h * (f[1] + 4 * f[2] + new_f) / 3
        while abs(y_corrected - y_predicted) > eps:
            y_predicted = y_corrected
            new_f = func(x, y_predicted)
            y_corrected = Y[-2] + h * (f[1] + 4 * f[2] + new_f) / 3
        Y.append(y_predicted)
        f = f[1:]
        f.append(new_f)

        output += str_result(i, x, y_predicted, new_f, exact(x))

        x += h
        i += 1
    return X, Y, output


def adams(func, a, b, y0, h, exact, eps=None):
    output = ""
    X, Y, out = runge_kutta_4th_order(func, a, a + 3.5 * h, y0, h, exact)
    output += out
    f = [func(X[i], Y[i]) for i in range(0, 4)]
    x = X[-1] + h
    i = 4
    while x <= b:
        df = f[-1] - f[-2]
        d2f = f[-1] - 2 * f[-2] + f[-3]
        d3f = f[-1] - 3 * f[-2] + 3 * f[-3] - f[-4]

        y_next = Y[-1] + h * f[-1] + (h ** 2) / 2 * df + 5 * (h ** 3) / 12 * d2f + 3 * (h ** 4) / 8 * d3f
        f_next = func(x, y_next)

        X.append(x)
        Y.append(y_next)
        f.append(f_next)

        output += str_result(i, x, y_next, f_next, exact(x))

        x += h
        i += 1
    return X, Y, output
