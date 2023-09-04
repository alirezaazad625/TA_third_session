from excersize.op import Operator


class Calculator:

    @staticmethod
    def add(first: float, second: float) -> float:
        return first + second

    @staticmethod
    def multiply(first: float, second: float) -> float:
        return first * second

    @staticmethod
    def subtract(first: float, second: float) -> float:
        return first - second

    @staticmethod
    def division(first: float, second: float) -> float:
        return first / second

    @classmethod
    def calculate(cls, param: Operator, first: float, second: float):
        match param:
            case Operator.ADD:
                return Calculator.add(first=first, second=second)
            case Operator.SUBTRACT:
                return Calculator.subtract(first=first, second=second)
            case Operator.MULTIPLY:
                return Calculator.multiply(first=first, second=second)
            case Operator.DIVISION:
                return Calculator.division(first=first, second=second)
