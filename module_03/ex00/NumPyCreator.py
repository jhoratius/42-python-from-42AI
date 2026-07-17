import sys
import string
import numpy as np

class NumpyCreator:
    # def __init__(self)

    def __str__(self):
        """Turns every data structure into NumPy structure"""
        return "Turns every data structure into NumPy structure"

    def from_list(self, lst):
        # if lst not isinstance list:

        if isinstance(lst, list) == False:
            return None
        return np.array(lst, dtype)

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple) == False:
            return None
        arr = np.array(tpl, dtype)
        print(arr)

    def from_iterable(self, itr):
        arr = np.array(list(itr))
        print(arr)

    def from_shape(self, shape, value):
        arr = np.array(tpl, dtype)
        print(arr)

    def random(self, shape):
        arr = np.array(shape)
        print(arr)

    def identity(self, n):
        print(np.identity(n))

    # • from_list(self, lst): takes a list or nested lists and returns its corresponding
    # Numpy array.

    # • from_tuple(self, tpl): takes a tuple or nested tuples and returns its correspond-
    # ing Numpy array.

    # • from_iterable(self, itr): takes an iterable and returns an array which contains
    # all of its elements.

    # • from_shape(self, shape, value): returns an array filled with the same value.
    # The first argument is a tuple which specifies the shape of the array, and the second
    # argument specifies the value of the elements. This value must be 0 by default.

    # • random(self, shape): returns an array filled with random values. It takes as an
    # argument a tuple which specifies the shape of the array.

    # • identity(self, n): returns an array representing the identity matrix of size n.