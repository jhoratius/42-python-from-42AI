#!/usr/bin/env python

    # count = 0
    # for str in tab:
    #     for char in str:
    #         if char not in string.punctuation:
    #             count +=1
    #     if count > N:
    #         filter_tab.append(str)
    #     count = 0

import sys
import string

def filterword(input_str: str, N: int):
    filter_tab = []
    tab = input_str.split()

    filter_tab = [ str_input for str_input in tab if len([char for char in str_input if char not in string.punctuation]) > N ]

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