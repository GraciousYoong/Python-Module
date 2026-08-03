from .elements import create_air, create_earth
from elements import create_fire, create_water

def healing_potion() -> str:
	return(f"Healing potion brewed with {create_earth} and {create_air}")


def strength_potion() -> str:
	pass

# A function healing_potion() that returns the string “Healing potion brewed with
# ’[created earth element]’ and ’[created air element]”.
# • A function strength_potion() that returns the string “Strength potion brewed
# with ’[created fire element]’ and ’[created water element]”.