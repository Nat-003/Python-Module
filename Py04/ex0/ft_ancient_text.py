def file_test() -> None:
    print("== CYBER ARCHIVES - DATA RECOVERY SYSTEM == \n")
    try:
        vault_path = "ancient_fragment.txt"
        f = open(vault_path)
        print(f"Accessing Storage Vault: {vault_path}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        print("\n")
        print("Data recovery complete. Storage unit disconncted.")
        f.close()
    except FileNotFoundError as e:
        print(f"file not found {e}")


if __name__ == "__main__":
    file_test()
