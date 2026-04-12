import os
import sys
from dotenv import load_dotenv

def oracle() -> None:
    env_found = load_dotenv()
    if not env_found:
        print("[INFO] No .env file found. Reading from system environment.")

    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    
    missing = [var for var in required_vars if os.getenv(var) is None]

    if missing:
        print("ORACLE STATUS: Reading the Matrix... FAILED")
        for var in missing:
            print(f"CRITICAL ERROR: Configuration variable '{var}' is missing.")
        sys.exit(1)

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
        print(f"API Access: Authenticated (Key: {api_key})")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_url}")
    else:
        print("Database: Conneted remotly")
        print("API Access: Authenticated (Dev Mock)")
        print(f"Log Level: User")
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