import numpy as np
import matplotlib.pyplot as plt

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)):

		x_max, y_max = array.shape()
		if dim[0] > x_max:
			assert 

		new_arr = array[position[0]:position[0] + dim[0], position[1]: position[1] + dim[1]]
		return new_arr

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

	# def thin(self, array, n, axis):

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

	# def juxtapose(self, array, n, axis):

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

	# def mosaic(self, array, dim):

	# Makes a grid with multiple copies of the array. The dim argument specifies
	# the number of repetition along each dimensions.

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
