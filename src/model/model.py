from typing import Union


class Model:
    number_1: int
    number_2: int

    def __init__(self):
        self.number_1 = 0
        self.number_2 = 0

    def calculate(self, option: str) -> Union[int, str]:
        if option == "+":
            return self.number_1 + self.number_2
        elif option == "-":
            return self.number_1 - self.number_2
        elif option == "*":
            return self.number_1 * self.number_2
        elif option == "/":
            if self.number_2 != 0:
                return self.number_1 // self.number_2
            else:
                return "Zero Division Error"
        else:
            return "Option Error"
