from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def shield(target: str, power: int) -> str:
    return f"Shield absorbs {power} damage from {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power : (spell1(target,power),spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target,power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(target, power) if condition(target, power) else "Spell fizzeled"



def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: list(map(lambda s: s(target, power), spells))


mega_fireball = power_amplifier(fireball, 3)
print(mega_fireball("Dragon", 20))

if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 20))


    print("\nTesting conditional caster...")
    condition = lambda target, power: True if power > 20 else False
    caster = conditional_caster(condition, fireball)
    print(caster("Mage", 25))
    print(caster("Dragon", 20))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning, shield])
    print(sequence("Elves", 40))
