import sys


def command_quest() -> None:
    i = 1
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No argument received")
    else:
        print(f"Argument received: {len(sys.argv) - 1}")
    print(f"prgram name: {sys.argv[0]}")
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total argument receive: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
