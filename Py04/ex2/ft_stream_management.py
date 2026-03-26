import sys


def manage_stream() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Input stream active. Enter archivist ID:")
    status = input("Input stream active. Enter status report:")
    print("\n")
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                     "verified\n")
    sys.stdout.write("[STANDARD] Data transmision complete\n")
    print("\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    manage_stream()
