#!/usr/bin/env python

import sys
import string

def counter(input: str, num: int):
    i = 0
    for char in input:
        if num == 0:
            if char.isupper():
                i += 1
        if num == 1:
            if char.islower():
                i += 1
        if num == 2:
            if char in string.punctuation:
                i += 1
        if num == 3:
            if char == ' ':
                i += 1
    return i

def count(input: str):

    length = 0
    upper_l = 0
    lower_l = 0
    punct = 0
    spaces = 0

    length = len(input)
    upper_l = counter(input, 0)
    lower_l = counter(input, 1)
    punct = counter(input, 2)
    spaces = counter(input, 3)

    print(f"The text contains {length} printable character(s):")
    print(f"{upper_l} upper letter(s)")
    print(f"{lower_l} lower letter(s)")
    print(f"{punct} punctuations")
    print(f"{spaces} space(s)")

def main():
    try:
        assert len(sys.argv) == 2, "Wrong number of arguments"

        try:
            input = sys.argv[1]
            count(input)
        except ValueError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()