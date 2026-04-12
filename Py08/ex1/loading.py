import importlib
import sys


def check_packages() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    packages = {"pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "matplotlib": "Visualization ready"}

    for package, des in packages.items():
        try:
            mod = importlib.import_module(package)
            print(f"[OK] {package} ({mod.__version__}) - {des}")
        except ModuleNotFoundError:
            print(F"[MISSING] {package} - Not installed")
            sys.exit("Install dependencies with: pip install"
                     " -r requirements.txt\n"
                     "Or with Poetry: poetry install")


def run_analysis() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randint(0, 100, 1000)
    df = pd.DataFrame(data, columns=["signal"])
    print(f"Mean value: {df['signal'].mean():.2f}")
    print(f"Max value: {df['signal'].max()}")
    print(f"Min value: {df['signal'].min()}")
    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.hist(df["signal"], bins=20)
    plt.title("Matrix Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

def compare_managers() -> None:
    print("\nDependency Management Comparison:")
    print("\npip:")
    print("  Uses requirements.txt to install dependencies")
    print("  Version pinning is manual (e.g. pandas==2.1.0)")
    print("  You manage the virtual environment separately")
    print("  Install with: pip install -r requirements.txt")
    print("\nPoetry:")
    print("  Uses pyproject.toml to install dependencies")
    print("  Version ranges are flexible (e.g. pandas^2.1.0)")
    print("  Automatically creates and manages the virtual environment")
    print("  Tries to install your project as a package by default")
    print("  Install with: poetry install")


if __name__ == "__main__":
    check_packages()
    run_analysis()
    compare_managers()