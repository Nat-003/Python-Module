def validate_ingredients(ingredients: str) -> str:
    from light_spellbook import light_spell_allowed_ingredients
    valid = light_spell_allowed_ingredients()
    for i in valid:
        if i in ingredients.lower():
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"