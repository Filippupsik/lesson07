from abc import ABC, abstractmethod
class Cloth(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def sum(self):
        return f"Общее количество затраченой ткани: {self.param / 6.5 + 0.5 + 2 * self.param+ 0.3 :.2f}"
    @abstractmethod
    def abstract(self):
        pass

class Coat(Cloth):
    def sum(self):
        return f"Ткани уходит на пальто: {self.param / 6.5 + 0.5 :.2f} ткани"
    def abstract(self):
        pass

class Costume(Cloth):
    def sum(self):
        return f"Ткани уходит на костюм: {2 * self.param+ 0.3 :.2f}"
    def abstract(self):
        pass

coat = Coat(400)
costume = Costume(55)
cloth = Cloth
print(coat.sum())
print(costume.sum())
print(cloth.sum())