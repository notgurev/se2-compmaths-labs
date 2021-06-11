from dataclasses import dataclass


@dataclass
class Result:
    integral_value: float
    partitions: int
    decimal_places: int
    additional_info: str = ''

    def __str__(self):
        return f'Результат{self.additional_info}:\n' \
               f'Значение интеграла: {round(self.integral_value, self.decimal_places)}\n' \
               f'Число разбиений интервала интегрирования: {self.partitions}\n'
