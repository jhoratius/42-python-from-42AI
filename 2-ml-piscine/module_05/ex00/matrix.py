import numpy as np

class Matrix:

    def __init__(self, arg):
        if isinstance(arg, list):
            self.data = arg
            rows = len(arg)
            cols = len(arg[0])
            self.shape = (rows, cols)

        elif isinstance(arg, tuple):
            print()
            self.data = [[[0] * arg[0]] * arg[1]]
            self.shape = arg

        else:
            raise TypeError("Data must be a list of lists or a shape tuple.")

    def __str__(self):
        return str(self.data)

    # def __repr__(self):
    
    def create_matrix(shape: tuple) -> list[list[float]]:
        rows, cols = shape
        res = [[0.0 for _ in range(cols)] for _ in range(rows)]
        return res

    # add : only matrices of same dimensions.
    def __add__(self, other):
        
        mat1 = self.data
        mat2 = other.data
        mat_res = [[0.0 for _ in range(mat1.shape[1])] for _ in range(mat2.shape[0])]
        for val1 in mat1:
            for val2 in mat2:
                mat_res[i][j] = val1 + val2
        # mat_res = [val1 + val2 for val1 in mat1, for val2 in mat2]
        return mat_res

    # def __radd__(self, other):
    #     mat1 = other.data
    #     mat2 = self.data
    #     mat_res = [val1 + val2 for val1 in mat1, for val2 in mat2]
    #     return mat_res

    # def __sub__(self, other):
    #     mat1 = self.data
    #     mat2 = other.data
    #     mat_res = [val1 - val2 for val1 in mat1, for val2 in mat2]
    #     return mat_res

    # def __rsub__(self, other):
    #     mat1 = other.data
    #     mat2 = self.data
    #     mat_res = [val1 - val2 for val1 in mat1, for val2 in mat2]
    #     return mat_res

    # def __truediv__(self, other):
    #     mat1 = other.data
    #     mat2 = self.data
    #     mat_res = [val1 / val2 for val1 in mat1, for val2 in mat2]
    #     return mat_res

    # def __rtruediv__(self, other):
    #     mat1 = self.data
    #     mat2 = other.data
    #     mat_res = [val1 / val2 for val1 in mat1, for val2 in mat2]
    #     return mat_res
    #     # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    #     # returns a Vector if we perform Matrix * Vector mutliplication.
    #     return np.__truediv__(other.data, self.data)
    # MN = (M[0][0] * N[0][0] + M[0][1] * N[1][0], M[0][0] * N[0][1] + M[0][1] * N[1][1])
        #  (M[0][0] * N[0][0] + M[0][1] * N[1][0], M[0][0] * N[0][1] + M[0][1] * N[1][1])

    # def __mul__(self, other):
    #     rows_A = len(self.data)
    #     cols_A = len(self.data[0])
    #     rows_B = len(other.data)
    #     cols_B = len(other.data[0])

    #     if cols_A != rows_B:
    #         raise ValueError(f"Cannot multiply matrices of shape ({rows_A}, {cols_A}) and ({rows_B}, {cols_B})")
        
    #     result = self.create_matrix((cols_B, rows_A))

    #     # 2 rows
    #     for i in range(rows_A):
    #         # 4 columns
    #         for j in range(cols_B):
    #             print()

    #     return result

    # def __rmul__(self, other):
    #     return np.dot(other.data, self.data)

    # def T():
