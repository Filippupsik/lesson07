class Cell:
    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        return f"Результат сложения: {self.param + other.param}"

    def __sub__(self, other):
        return f"Результат вычитания: {self.param - other.param}"

    def __truediv__(self, other):
        return f"Результат деления: {self.param // other.param}"

    def __mul__(self, other):
        return f"Результат умножения: {self.param * other.param}"

    def make_order(self, row):
        result = ''
        for i in range(int(self.param / row)):
            result += '*' * row + '\n'
        result += '*' * (self.param % row) + '\n'
        return result



cell = Cell(25)
cell_2 = Cell(4)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(6))