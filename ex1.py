class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f"{i:3}", end="")
            print()
        return ""
    def __add__(self, other):
        for i in range(len(self.matrix)):
            for i_2 in range(len(other.matrix[i])):
                self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
        return Matrix.__str__(self)

m_1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
m_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m_1 + m_2)
