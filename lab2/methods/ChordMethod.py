from Result import Result
from methods.Method import Method


class ChordMethod(Method):
    name = 'Метод хорд'

    def check(self):
        # Анализировать наличие корня на введенном интервале.
        root_exists = self.equation.root_exists(self.left, self.right)
        return root_exists, 'Отсутствует корень на заданном промежутке' if not root_exists else ''

    def solve(self) -> Result:
        # Удобные имена
        f = self.equation.function
        a = self.left
        b = self.right
        epsilon = self.epsilon
        # Итерации
        prev = float("inf")
        iteration = 0
        while True:
            iteration += 1
            fa = f(a)
            fb = f(b)
            x = (a * fb - b * fa) / (fb - fa)
            fx = f(x)
            if self.log:
                print(f'{iteration}: a = {a:.3f}, b = {b:.3f}, x = {x:.3f}, '
                      f'f(a) = {fa:.3f}, f(b) = {fb:.3f}, f(x)={fx:.3f}, |a-b| = {abs(a - b):.3f}')
            if abs(x - prev) <= epsilon:
                break
            if fa * fx < 0:
                b = x
            else:
                a = x
            prev = x
        return Result(x, fx, iteration, self.decimal_places)
