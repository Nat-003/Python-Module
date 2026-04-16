from typing import Callable


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumutalor(initial_power: int) -> Callable:
    def accumulator(amout: int) -> int:
        nonlocal initial_power
        initial_power += amout
        return initial_power
    return accumulator
        

def enchantment_factory(enchantement_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        nonlocal enchantement_type
        return f"{enchantement_type} {item_name}"
    return enchantment


def memory_vault() -> dict:
    storage = {}

    def store(key, value):
       storage[key] = value

    def recall(key):
        return storage.get(key,"Memory not found") 

    return {"store": store, "recall": recall}

test = mage_counter()
for i in range(10):
    print(test())
print(test())

test2 = spell_accumutalor(100)
print(test2(20))
print(test2(20))

test3 = enchantment_factory("Flaming")
print(test3("Sword"))