import sys

def whois(input: int):

	if input == 0:
		print("I'm Zero.")
		return
	if input % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

def main():
    try:
        assert len(sys.argv) == 2, "Wrong number of arguments"
        try:
            val = int(sys.argv[1])
            whois(val)
        except ValueError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()