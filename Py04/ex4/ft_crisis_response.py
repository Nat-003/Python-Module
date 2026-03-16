def crisis_response(file_name) -> None:
    try:
        with open(file_name) as f:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered- ``{f.read()}``")
            print("STATUS: Normal operations resumed")
            print("\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print("\n")
    except PermissionError:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def crisis_tester() -> None:
    file1 = "lost_archive.txt"
    file2 = "classified_vault.txt"
    file3 = "standard_archive.txt"
    files = [file1, file2, file3]
    for file in files:
        crisis_response(file)


if __name__ == "__main__":
    crisis_tester()
    print("All crisis scenarios handled successfully. Archives secure.")
