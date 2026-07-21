#!/usr/bin/env python

import sys
import string

def count(A: int, B: int):
    print("Sum       :", A + B)
    print("Difference:", A - B)
    print("Product   :", A * B)
    if B == 0:
        print("Quotient  : ERROR (division by zero)")
        print("Remainder : ERROR (modulo by zero)")
    else:
        print("Quotient  :", A / B)
        print("Remainder :", A % B)


def main():
    try:
        if len(sys.argv) != 3:
            print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
            return
        try:
            count(int(sys.argv[1]), int(sys.argv[2]))
        except ValueError as e:
            raise e
    except ValueError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()