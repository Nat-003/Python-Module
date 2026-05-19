from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any

test_spells = [1, 4, 3, 2, 7, 8]


def shield(target: str, power: int, element: str) -> str:
    return f"Shield absorbs {power} of {element} damage from {target}"


def spell_reducer(spells: list[int], operation: str) -> int | str:
    if not spells:
        return 0
    if operation.lower() == "add":
        return reduce(lambda a, b: b + a, spells)
    elif operation.lower() == "multiply":
        return reduce(lambda a, b: a * b, spells)
    elif operation.lower() == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation.lower() == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError(f"Operation not supported: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    v1 = partial(base_enchantment, power=50, element="water")
    v2 = partial(base_enchantment, power=50, element="fire")
    v3 = partial(base_enchantment, power=50, element="wind")
    new_versions = {"water": v1,
                    "fire": v2,
                    "wind": v3}
    return new_versions


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatch.register(str)
    def _(args: str) -> str:
        return f"Enchantment: {args}"

    @dispatch.register(list)
    def _(args: list) -> str:
        return f" Multi-cast: {len(args)}"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(shield)
    print(enchanters["fire"]("Dragon"))

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "wind"]))
    print(dispatch(3.14))
