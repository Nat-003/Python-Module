def garden_operations(error_type: str):
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        1 / 0
    elif error_type == "file":
        open("ghost_plant.txt")
    elif error_type == "key":
        {}["missing_key"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError")
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError")
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError")
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError:  {e} \n")

    try:
        print("Testing KeyError")
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing plant \n")

    try:
        print("Testing multiple errors together...")
        garden_operations("file")
    except (FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
