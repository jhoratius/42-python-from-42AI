#!/usr/bin/env python

import sys
import string
import datetime as dt

kata = (2019, 9, 25, 3, 30)

def printing():
    assert 1 <= len(str(kata[0])) <= 4 and 1 <= kata[0] <= 2026, "year over limits"
    assert 1 <= len(str(kata[1])) <= 2 and 1 <= kata[1] <= 12, "months over limits"
    assert 1 <= len(str(kata[2])) <= 2 and 1 <= kata[2] <= 31, "day over limits"
    assert 1 <= len(str(kata[3])) <= 2 and 1 <= kata[3] <= 24, "hours over limits"
    assert 1 <= len(str(kata[4])) <= 2 and 1 <= kata[4] <= 59, "minutes over limits"

    print(f"{kata[1]:02d}/{kata[2]:02d}/{kata[0]:04d} {kata[3]:02d}:{kata[4]:02d}")

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