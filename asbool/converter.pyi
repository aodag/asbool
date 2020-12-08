from typing import Any, Sequence


class AsBoolConverter(object):
    def __init__(self, true_values: Sequence[str], false_values: Sequence[str]):
        pass

    def __call__(self, ss: Any) -> bool:
        pass