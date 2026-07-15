#!/usr/bin/env python

import sys
import string

def filterword(input_str: str, N: int):
    filter_tab = []
    tab = input_str.split()
    # print(tab)
    count = 0

    for str in tab:
        for char in str:
            if char not in string.punctuation:
                count +=1
        if count > N:
            filter_tab.append(str)
        count = 0
    print(filter_tab)

def main():
    if len(sys.argv) != 3:
        print("ERROR")
        sys.exit()

    try:
        filterword(sys.argv[1], int(sys.argv[2]))
    except ValueError:
        print("ERROR")
    except AssertionError:
        print("ERROR")

if __name__ == "__main__":
    main()