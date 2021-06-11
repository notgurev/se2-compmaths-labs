from calculate import calculate_value
from methods.Method import Method


class TrapezoidalMethod(Method):
    name = "Метод трапеций"

    @staticmethod
    def integrate(f, a, b, partitions) -> float:
        step = (b - a) / partitions
        result = 0
        x = a
        while x < b:
            result += (calculate_value(f, x) + calculate_value(f, x + step)) / 2 * step
            x += step
        return result
