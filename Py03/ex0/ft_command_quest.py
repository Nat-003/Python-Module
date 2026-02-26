import sys


def command_quest() -> None:
    i = 1
    print("=== Command Quest ===")
    print(f"Argument received: {len(sys.argv) - 1}")
    print(f"prgram name: {sys.argv[0]}")
    arg_list = sys.argv[1:]
    for arg in arg_list:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total argument receive: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
