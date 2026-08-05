from .. import potions
from elements import create_fire
from alchemy.elements import create_air


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and "
        f"'{potions.strength_potion()}' mixed with "
        f"'{create_fire()}'\n"
    )
