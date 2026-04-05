from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    valid = dark_spell_allowed_ingredients()
    for i in valid:
        if i in ingredients.lower():
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"