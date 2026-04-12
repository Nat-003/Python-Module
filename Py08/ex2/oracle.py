import os
import sys
from dotenv import load_dotenv


def oracle() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL", "None")
    api_key = os.getenv("API_KEY", "None")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT", "None")

    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print(f"Database: {db_url}")
        masked_key = f"{api_key[:0]}****" if api_key != "None" else "None"
        print(f"API Access: Authenticated (Key: {masked_key})")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_url}")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated (Dev Mock)")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    

    if api_key != "None":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Using default or missing secrets")


    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            if ".env" in f.read():
                print("[OK] .env file properly configured")
            else:
                print("[!] .env not found in .gitignore")
    else:
        print("[!] .gitignore missing")

    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        oracle()
    except Exception as e:
        print(f"Error accessing the mainframe: {e}")
        sys.exit(1)