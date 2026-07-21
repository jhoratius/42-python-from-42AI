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

        if not isinstance(lst, list):
            print("is not a list")
            return None
        
        if lst and isinstance(lst[0], list):
            if any(len(row) != len(lst[0]) for row in lst):
                return None

        return np.array(lst)

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple) == False:
            return None
        arr = np.array(tpl)
        print(arr)

    def from_iterable(self, itr):
        arr = np.array(list(itr))
        print(arr)

    def from_shape(self, shape, value):
        arr = np.full(shape, value)
        print(arr)

    def random(self, shape):
        arr = np.random.random(shape)
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