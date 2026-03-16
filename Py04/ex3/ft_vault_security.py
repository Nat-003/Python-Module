def vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_name = "classified_data.txt"
    file_name2 = "preserved_data.txt"
    try:
        with open(file_name) as f:
            print("SECURE EXTRACTION:")
            print(f.read())
            print("\n")
        with open(file_name2, 'w') as f2:
            print("SECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
            f2.write("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion \n")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError as e:
        print(f"This file {e} does not exist")


if __name__ == "__main__":
    vault_security()
