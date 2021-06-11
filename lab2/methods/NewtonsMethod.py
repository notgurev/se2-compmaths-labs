from scipy.misc import derivative

from Result import Result
from methods.Method import Method

dx = 0.00001


class NewtonsMethod(Method):
    name = 'Метод Ньютона'

    def solve(self) -> Result:
        f = self.equation.function
        prev = self.choose_initial_x()

        iteration = 0
        while True:
            iteration += 1
            dfprev = derivative(f, prev, dx)
            fprev = f(prev)
            x = prev - fprev / dfprev
            diff = abs(x - prev)
            if self.log:
                print(f'{iteration}: xk = {prev:.3f}, f(xk) = {fprev:.3f}, '
                      f'f\'(xk) = {dfprev:.3f}, xk+1 = {x:.3f}, |xk - xk+1| = {diff:.3f}')
            if diff <= self.epsilon:
                break
            prev = x

        return Result(x, f(x), iteration, self.decimal_places)

    def choose_initial_x(self) -> float:
        a = self.left
        b = self.right
        f = self.equation.function
        # выбираем по условию быстрой сходимости (если получится)
        return a if f(a) * derivative(f, a, dx, 2) > 0 else b
