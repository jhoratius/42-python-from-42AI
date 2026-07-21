import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
# arr1 = np.arange(0,25).reshape(5,5)
# print(arr1)
# print(spb.crop(arr1, (3,1),(1,0)))

# arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
# print(arr2)
# print("")
# print(spb.thin(arr2,3,0))
# print("")

# arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
# print(arr3)
# print("")
# print(spb.juxtapose(arr3, 3, 1))
# print("")

arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(arr4)
print("")
print(spb.mosaic(arr4, (3, 3)))