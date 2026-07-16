#!/usr/bin/env python

import sys
import string

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def display():
	for k, v in kata.items():
		print(f"{k} was created by {v}")

def main():
    try:
        assert len(sys.argv) > 0, "Wrong number of arguments"
        try:
            display()
        except AssertionError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()