import numpy as np
import matplotlib.pyplot as plt

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):

        x_max, y_max = array.shape
        try:
            if dim[0] < 0 or dim[0] > x_max:
                raise ValueError("over the boundaries")
            if dim[1] < 0 or dim[1] > y_max:
                raise ValueError("over the boundaries")
            if position[0] < 0 or position[0] >= x_max:
                raise ValueError("over the boundaries")
            if position[1] < 0 or position[1] >= y_max:
                raise ValueError("over the boundaries")

            if position[0] + dim[0] > x_max or position[1] + dim[1] > y_max:
                raise ValueError("over the boundaries")

            new_arr = array[position[0]:position[0] + dim[0], position[1]: position[1] + dim[1]]
            return new_arr
        except Exception as e:
            print(f"Error: {e}")
    # Crops the image as a rectangle via dim arguments (being the new height
    # and width of the image) from the coordinates given by position arguments.

    # Args:
    # -----
    # array: numpy.ndarray
    # dim: tuple of 2 integers.
    # position: tuple of 2 integers.

    # Returns:
    # -------
    # new_arr: the cropped numpy.ndarray.
    # None: (if the combination of parameters is not possible).

    # Raises:
    # ------
    # This function should not raise any Exception.

    def thin(self, array, n, axis):

        x_max, y_max = array.shape
        try:
            if n > x_max or n > y_max:
                raise ValueError("Over the boundaries.")
            if axis < 0 or axis > 1:
                raise ValueError("Wrong axis.")

            # i = 0
            # new_arr = array
            # while(i < n):
            #     new_arr = np.delete(array, i, axis)
            #     i += 1
            new_arr = np.delete(array, np.s_[0:n], axis)
            return (new_arr)

        except Exception as e:
            print(f"Error: {e}")

    # Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)

    # Args:
    # -----
    # array: numpy.ndarray
    # n: non null positive integer lower than the number of row/column of the array
    # (depending of axis value).
    # axis: positive non null integer.

    # Returns:
    # -------
    # new_arr: thined numpy.ndarray.
    # None: (if the combination of parameters is not possible).

    # Raises:
    # ------
    # This function should not raise any Exception.

    def juxtapose(self, array, n, axis):
        reps = [1] * array.ndim
        reps[axis] = n
        return np.tile(array, reps)

    # Imagine you have a grayscale image (array.ndim = 2). You want to tile it horizontally (axis = 1) and make n = 3 copies.
    # Line 1: reps = [1] * array.ndim
    # Since ndim is 2, this creates:
    # reps = [1, 1] (Default: Don't repeat rows, don't repeat columns)
    # Line 2: reps[axis] = n
    # Since axis = 1 and n = 3, this changes the value at index 1:
    # reps[1] = 3
    # Now, reps becomes: [1, 3]
    # When you pass [1, 3] to np.tile(), it looks at the instructions: "Repeat rows 1 time (no change), repeat columns 3 times." You get a perfect horizontal strip of 3 images.

    # Juxtaposes n copies of the image along the specified axis.

    # Args:
    # -----
    # array: axis:numpy.ndarray.
    # n: positive non null integer.
    # axis: integer of value 0 or 1.

    # Returns:
    # -------
    # new_arr: juxtaposed numpy.ndarray.
    # None: (if the combination of parameters is not possible).

    # Raises:
    # -------
    # This function should not raise any Exception.

    def mosaic(self, array, dim):

        new_arr = self.juxtapose(array, dim[0], 0)
        new_arr = self.juxtapose(new_arr, dim[1], 1)
        return new_arr
        # reps = [1] * dim
        # reps[0] = dim
        # new_arr = np.tile(array, reps)
        # reps2 = [1] * dim
        # reps2[1] = dim
        # new_arr = np.tile(array, reps2)

    # Makes a grid with multiple copies of the array. The dim argument specifies the number of repetition along each dimensions.

    # Args:
    # -----
    # array: tuple of 2 integers.
    # dim: numpy.ndarray.

    # Return:
    # -----
    # new_arr: mosaic numpy.ndarray.
    # None (combinaison of parameters not compatible).

    # Raises:
    # -------
    # This function should not raise any Exception.
