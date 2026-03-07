from sys import argv


def is_even_or_odd(number: int):
    if number % 2 == 0:
        return print("I'm Even.")
    return print("I'm Odd.")


def main():
    if len(argv) > 2:
        return print("AssertionError: more than one argument is provided")

    if len(argv) < 2:
        return

    try:
        number = int(argv[1])
        is_even_or_odd(number)
        return
    except ValueError:
        print("AssertionError: argument is not an integer")
        return


if __name__ == "__main__":
    main()
