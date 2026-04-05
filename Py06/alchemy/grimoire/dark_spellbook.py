from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredient: str) -> str:
    valid = validate_ingredients(ingredient)
    if valid == "VALID":
        return f"Spell recorded: {spell_name} {ingredient}"
    elif valid == "INVALID":
        return "rejected"