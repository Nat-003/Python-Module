def write_in_file() -> None:
    print("=== CYBER ARCHIVES PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    f = open(file_name, 'w')
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    for entry in entries:
        print(entry)
        f.write(entry + "\n")
    f.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    write_in_file()
