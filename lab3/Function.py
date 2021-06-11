import math
from dataclasses import dataclass
from typing import Callable


@dataclass
class Function:
    function: Callable
    text: str
    symmetrical: bool = False
    symmetry_point: float = math.inf
