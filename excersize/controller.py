from excersize.calculator import Calculator
from excersize.op import Operator


class Controller:

    @staticmethod
    def calculate(args: list[str]) -> str | float:
        if len(args) != 3:
            return f"You should exactly give 3 arguments.\nGiven arguments count: {len(args)}."

        if args[0] not in Operator.values():
            return f"{args[0]} operator does not exist."

        try:
            first = float(args[1])
        except ValueError:
            return f"{args[1]} parameter must be of type float."

        try:
            second = float(args[2])
        except ValueError:
            return f"{args[2]} parameter must be of type float."

        return Calculator.calculate(Operator(args[0]), first=first, second=second)
