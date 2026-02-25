def get_total(dick: dict) -> int:
    total = 0
    for item in dick.values():
        for i in item.values():
            total += i
    return total


def show_inventory(dick: dict, total: int) -> None:
    for i, j in dick.items():
        for quantity in j.values():
            percent = quantity / total * 100
            print(f"{i}: {quantity} units ({percent:.2f})")


def find_most(dick: dict) -> None:
    max = 0
    item = None
    for name, quantity in dick.items():
        for q in quantity.values():
            if max < q:
                max = q
                item = name
    print(f"Most abundant: {item} ({max})")


def find_least(dick: dict) -> None:
    min = 10
    item = None
    for name, quantity in dick.items():
        for q in quantity.values():
            if min > q:
                min = q
                item = name
    print(f"Least abundant: {item} ({min})")


def moderate_scarce(dick: dict) -> None:
    moderate = {}
    scare = {}
    for name, quantity in dick.items():
        for q in quantity.values():
            if q < 5:
                scare.update({name: q})
            else:
                moderate.update({name: q})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scare}")


def restock(dick: dict) -> None:
    restock = {}
    for name, quantity in dick.items():
        for q in quantity.values():
            if q == 1:
                restock.update({name: q})
    print("Restock suggestion: ", end="")
    for r in restock.keys():
        print(f"{r}, ", end="")


def is_in_dict(dick: dict, items: str) -> bool:
    for i in dick.keys():
        if items == i:
            return True
    return False


def inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {
                "potion": {"quantity": 5},
                "armor": {"quantity": 3},
                "shield": {"quantity": 2},
                "sword": {"quantity": 1},
                "helmet": {"quantity": 1}
                }
    total = get_total(inventory)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}\n")
    print("=== Curent Inventory ===")
    show_inventory(inventory, total)
    print("\n")
    print("=== Inventory Statistics ===")
    find_most(inventory)
    find_least(inventory)
    print("\n")
    print("=== Item Categories ===")
    moderate_scarce(inventory)
    print("\n")
    print("=== Management Sugestion ===")
    restock(inventory)
    print("\n")
    print("=== Dictionary Propertes Demo ===")
    print("Dictionary keys:", end="")
    for i in inventory.keys():
        print(f"{i}, ", end="")
    print("\n")
    print("Dictionary values: ", end="")
    for i, quantity in inventory.items():
        for q in quantity.values():
            print(f"{q}, ", end="")
    print("\n")
    test = is_in_dict(inventory, "merde")
    print(f"Sample lookup - 'sword' in inventory: {test}")


if __name__ == "__main__":
    inventory_system()
