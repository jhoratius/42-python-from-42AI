
import sys
import string
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

class ImageProcessor:        

    def load(self, path):
        try:
            arr = plt.imread(path)
            print(arr.shape[:2])
            return arr
        except Exception as e:
            print(f"Error: {e}")
            return None

    def display(self, array):
        try:
            plt.imshow(array)
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(f"Error: {e}")
            


