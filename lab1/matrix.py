def find_dominant_index(coefficients: []) -> (int, bool):
    """
    :param coefficients: row of coefficients from a matrix
    :return: tuple of: 0. index of dominant element or None if its not present; 1. is it strict or not
    """
    for i in range(len(coefficients)):
        coefficient_abs_sum = sum(list(map(abs, coefficients)))
        diff = 2 * abs(coefficients[i]) - coefficient_abs_sum
        if diff >= 0:
            return i, diff != 0
    return None, False


class Matrix:
    def __init__(self, size: int, data: [], right=None):
        self.coefficients = data
        self.size = size
        # optional right side of equation
        self.right = right

    def __str__(self):
        result = []
        for i in range(self.size):
            left = ''
            for j in range(self.size):
                left += f'{self.coefficients[i][j]:7.2f}'
            right = '  |' + f"{self.right[i]:7.2f}" if self.right is not None else ''
            result.append(left + right)
        return '\n'.join(result)

    @property
    def diagonally_dominant(self) -> bool:
        at_least_one_strict = False
        for row in range(self.size):
            (dominant_index, strict) = find_dominant_index(self.coefficients[row])
            if dominant_index != row:
                return False
            if strict:
                at_least_one_strict = True
        return True and at_least_one_strict

    def make_diagonally_dominant(self) -> bool:
        new_data = [None] * self.size
        new_right = [0] * self.size
        for row in range(self.size):
            # find index of dominant element in row
            (dominant_index, _) = find_dominant_index(self.coefficients[row])
            # if present and unique, add to new data
            if (dominant_index is not None) and (new_data[dominant_index] is None):
                new_data[dominant_index], new_right[dominant_index] = self.coefficients[row], self.right[row]
            else:
                return False
        # save changes
        self.coefficients, self.right = new_data, new_right
        return True
