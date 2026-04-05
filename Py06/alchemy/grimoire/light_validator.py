from light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    valid = light_spell_allowed_ingredients()
    if ingredients in valid:
        return "VALID"
    else:
        return "INVALID"