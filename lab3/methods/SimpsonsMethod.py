from calculate import calculate_value
from methods.Method import Method


class SimpsonsMethod(Method):
    name = "Метод Симпсона"

    @staticmethod
    def integrate(f, a, b, partitions) -> float:
        step = (b - a) / partitions
        result = calculate_value(f, a) + calculate_value(f, b)
        x = a + step
        i = 1
        while x < b:
            result += (4 * calculate_value(f, x) if (i % 2 == 0) else 2 * calculate_value(f, x))
            x += step
            i += 1
        return result * step / 3
