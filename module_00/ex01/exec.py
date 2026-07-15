import sys

def reverse_str(input: str) -> str:

    # List comprehension with condition
    swapped = "".join([char.upper() if char.islower() else char.lower() for char in input])
    # print(f"swapped : {swapped}")

    # Reverse the string using Python slicing
    return swapped[::-1]

def main():
    try:
        assert len(sys.argv) == 2, "Wrong number of arguments"
        try:
            new_rev_str = reverse_str(sys.argv[1])
            print(new_rev_str)
        except AssertionError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()