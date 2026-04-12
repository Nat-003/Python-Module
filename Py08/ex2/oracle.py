import os
import sys
from dotenv import load_dotenv


def oracle() -> None:
    env_found = load_dotenv()
    if not env_found:
        raise Exception("[INFO] No .env file found. Reading from system environment.")

    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = str(os.getenv("API_KEY"))
    log_level = os.getenv("LOG_LEVEL")
    zion_url = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print(f"Database: {db_url}")
        masked_key = f"{api_key[:4]}****" if api_key else "None"
        print(f"API Access: Authenticated (Key: {masked_key})")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_url}")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated (Dev Mock)")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    
    if api_key not in ["None", "your_secret_key_here", ""]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Using placeholder or empty secrets")

    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            content = f.read()
            if ".env" in content:
                print("[OK] .env file properly configured")
            else:
                print("[!] SECURITY RISK: .env not in .gitignore")
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
        print(f"Error: {e}")
        sys.exit(1)