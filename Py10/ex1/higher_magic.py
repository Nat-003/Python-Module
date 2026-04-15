from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def shield(target: str, power: int) -> str:
    return f"Shield absorbs {power} damage for {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power : (spell1(target,power),spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target,power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(target, power) if condition(target, power) else "Spell fizzeled"



def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: list(map(lambda s: s(target, power), spells))


# → ('Fireball hits Dragon for 10 damage', 'Heal restores Dragon for 10 HP')
mega_fireball = power_amplifier(fireball, 3)
print(mega_fireball("Dragon", 20))

if __name__ == "__main__":

    # your two spell definitions (fireball, heal)

    # test spell_combiner
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))

    # test power_amplifier
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 20))

    # test conditional_caster
    print("\nTesting conditional caster...")
    condition = lambda target, power: True if power > 20 else False
    caster = conditional_caster(condition, fireball)
    print(caster("Mage", 25))  # should cast
    print(caster("Dragon", 20))  # should fizzle

    # test spell_sequence
    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning, shield])
    print(sequence("Elves", 40))