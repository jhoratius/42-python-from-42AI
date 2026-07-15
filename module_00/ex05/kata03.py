#!/usr/bin/env python

import sys
import string

kata = (0, 4, 132.42222, 10000, 12345.67)

def printing():
    length = len(kata)
    assert 0 <= length <= 42, "string higher than 42"
    print(f"{'-' * (41 - length)}{kata}")

def main():
    try:
        assert len(sys.argv) != 0, "Wrong number of arguments"
        try:
            printing()
        except AssertionError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()