#!/usr/bin/env python

import sys
import string

kata = (0, 4, 132.42222, 10000, 12345.67)

def printing():
	print(f"module_0{kata[0]}, ex_0{kata[1]} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")

def main():
    try:
        assert len(sys.argv) > 0, "Wrong number of arguments"
        try:
            printing()
        except AssertionError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()