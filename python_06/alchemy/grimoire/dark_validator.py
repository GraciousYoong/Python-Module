from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    text = ingredients.lower()

    for item in allowed:
        if item in text:
            return f"({ingredients} - VALID)"

    return f"({ingredients} - INVALID)"
