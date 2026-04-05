from light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredient: str) -> str:
    valid = validate_ingredients(ingredient)
    if valid == "VALID":
        return f"Spell recorded: {spell_name} {ingredient}"
    elif valid == "INVALID":
        return "rejected"