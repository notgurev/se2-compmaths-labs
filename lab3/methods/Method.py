from Function import Function
from typing import Callable, Tuple

from Result import Result

class Method:
    name = None

    @staticmethod
    def integrate(f, a, b, partitions) -> float:
        pass

    @staticmethod
    def iterate(function, integrate_func, a: float, b: float, epsilon) -> Tuple[float, int]:
        partitions = 4
        last = integrate_func(function, a, b, partitions)
        while True:
            partitions *= 2
            current = integrate_func(function, a, b, partitions)
            diff = abs(current - last)
            if diff < epsilon:
                break
            last = current

        return current, partitions

    def solve(self, function: Function, a: float, b: float, epsilon: float, decimal_places: int) -> list[Result]:
        current, partitions = self.iterate(function.function, self.integrate, a, b, epsilon)
        return [Result(current, partitions, decimal_places)]
