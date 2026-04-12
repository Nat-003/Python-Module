    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            content = f.read()
            if ".env" in content:
                print("[OK] .env file properly configured")
            else:
                print("[!] SECURITY RISK: .env not in .gitignore")
    else:
        print("[!] .gitignore missing")