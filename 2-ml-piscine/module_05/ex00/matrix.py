import numpy as np

class Matrix:
    def __init__(self, data: list[list[float]] = [[1.0, 2.0], [3.0, 4.0]], shape: tuple[int, int] = (0, 0)):
        self.data = data
        self.shape = shape

    def __str__(self):
        """Matrix class"""
        return "Matrix class"
    
    # def __repr__(self):

    # add : only matrices of same dimensions.
    def __add__(self, Matrix):
        # make the addition of two matrices
        return self.Matrix.add(Matrix)

    def __radd__(self, Matrix):
        # sub : only matrices of same dimensions.
        return Matrix.add(self.Matrix)

    def __sub__(self, Matrix):
        return self.Matrix.sub(Matrix)

    def __rsub__(self, Matrix):
        # div : only scalars.
        return Matrix.sub(Matrix, self.Matrix)

    def __truediv__(self, Matrix):
        return np.__truediv__(self.Matrix, Matrix)

    def __rtruediv__(self, Matrix):
        # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
        # returns a Vector if we perform Matrix * Vector mutliplication.
        return np.__truediv__(Matrix, self.Matrix)

    def __mul__(self, Matrix):
        return self.Matrix * Matrix

    def __rmul__(self, Matrix):
        return Matrix * self.Matrix

    # def T():
