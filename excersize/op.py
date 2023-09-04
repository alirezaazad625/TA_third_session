from enum import Enum


class Operator(Enum):
    ADD = 'add'
    SUBTRACT = 'sub'
    DIVISION = 'div'
    MULTIPLY = 'mul'

    @staticmethod
    def values() -> list[str]:
        return [item.value for item in Operator]
