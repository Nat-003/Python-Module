import sys


def total_item(inventory: dict) -> int:
    total = 0
    try:
        for i in inventory.values():
            num = int(i)
            total += num
    except ValueError as e:
        print(f"Error {e}")
    return total


def show_inventory(inventory: dict, total: int) -> None:
    for i, q in inventory.items():
        percent = int(q) / total * 100
        print(f"{i}: {q} units ({percent:.2f})")


def inventory_stats(inventory: dict) -> None:
    max = 0
    least = 10000
    least_name = ""
    max_name = ""
    for i, q in inventory.items():
        num = int(q)
        if num > max:
            max = num
            max_name = i
        if least > num:
            least = num
            least_name = i
    print(f"Most abundant: {max_name} ({max} units)")
    print(f"Least abundant: {least_name} ({least} units)")


def moderate_scarce(inventory: dict) -> None:
    moderate = {}
    scarce = {}
    for i, q in inventory.items():
        if int(q) >= 5:
            moderate.update({i: q})
        elif int(q) < 5:
            scarce.update({i: q})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def management_sugestions(inventory: dict) -> None:
    restock = {}
    for i, q in inventory.items():
        if int(q) <= 1:
            restock.update({i: q})
    print("Restock suggestion: ", end="")
    for r in restock.keys():
        print(f"{r}, ", end="")


def is_in_dict(dick: dict, items: str) -> bool:
    for i in dick.keys():
        if items == i:
            return True
    return False


def dictio_demo(inventory: dict) -> None:
    print("Dictionary keys:", end="")
    for i in inventory.keys():
        print(f"{i}, ", end="")
    print("\n")
    print("Dictionary values: ", end="")
    for q in inventory.values():
        print(f"{q}, ", end="")
    print("\n")
    test = is_in_dict(inventory, "sword")
    print(f"Sample lookup - 'sword' in inventory: {test}")


def inventory_system() -> None:
    inventory = {}
    print("=== Invetory System Analysis ===\n")
    for arg in sys.argv[1:]:
        x = arg.split(":")
        inventory.update({x[0]: x[1]})
    total = total_item(inventory)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}\n")
    print("=== Current Inventory ===")
    show_inventory(inventory, total)
    print("\n")
    print("=== Inentory Statistics ===")
    inventory_stats(inventory)
    print("\n")
    print("=== Item Categories ===")
    moderate_scarce(inventory)
    print("\n")
    print("=== Management Suggestions ===")
    management_sugestions(inventory)
    print("\n")
    print("=== Dictionary Propertes Demo ===")
    dictio_demo(inventory)


if __name__ == "__main__":
    inventory_system()
