from matrix import Matrix 

m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
m1.shape
# Output:
# (3, 2)

# m1.T()
# # Output:
# # Matrix([[0., 2., 4.], [1., 3., 5.]])

# m1.T().shape
# # Output:
# # (2, 3)

# m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])
# m1.shape
# # Output:
# # (2, 3)

# m1.T()
# # Output:
# # Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

# m1.T().shape
# # Output:
# # (3, 2)

# m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
#              [0.0, 2.0, 4.0, 6.0]])
# m2 = Matrix([[0.0, 1.0],
#              [2.0, 3.0],
#              [4.0, 5.0],
#              [6.0, 7.0]])

m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])

m2 = Matrix([
    [0.0, 1.0],
    [2.0, 3.0],
    [4.0, 5.0],
    [6.0, 7.0]
])

print(f"add: {m1 + m2}")
print(f"radd: {m2 + m1}")
print(f"sub: {m1 - m2}")
print(f"rsub: {m2 - m1}")
print(f"truediv: {m1 / m2}")
print(f"rtruediv: {m2 / m1}")



m3 = Matrix((2,2))
print(m3)

# print(m1 * m2)
# # Output:
# # Matrix([[28., 34.], [56., 68.]])

# m1 = Matrix([[0.0, 1.0, 2.0],
# [0.0, 2.0, 4.0]])
# v1 = Vector([[1], [2], [3]])
# m1 * v1
# # Output:
# # Matrix([[8], [16]])

# Or: Vector([[8], [16]
# v1 = Vector([[1], [2], [3]])
# v2 = Vector([[2], [4], [8]])
# v1 + v2
# # Output:
# # Vector([[3],[6],[11]])


# v1 = Vector([[1, 2, 3]]) # create a row vector
# v2 = Vector([[1], [2], [3]]) # create a column vector
# v3 = Vector([[1, 2], [3, 4]]) # return an error