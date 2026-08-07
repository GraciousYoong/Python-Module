from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()

    text = ingredients.lower()

    for item in allowed:
        if item in text:
            return f"({ingredients} - VALID)"

    return f"({ingredients} - INVALID)"
