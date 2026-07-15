#!/usr/bin/env python

import sys
import string

cookbook = {
	'ingredients': {},
	'meal' = '',
	'prep_time' = 0
}

def create_meals():
	Sandwich = cookbook{}
	print(f"The 3 numbers are: {kata[0]}, {kata[1]}, {kata[2]}")
    
def main():
    try:
        assert len(sys.argv) > 0, "Wrong number of arguments"
        try:
            create_meals()
        except AssertionError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()