#!/usr/bin/env python

import sys
import string

kata = "The right format"

def printing():
    length = len(kata)
    assert 0 <= length <= 42, "string higher than 42"
    print(f"{'-' * (42 - length)}{kata}", end='')

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