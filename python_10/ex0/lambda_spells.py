# ============================================================
# EX0 - LAMBDA SANCTUM
# ============================================================
#
# MAIN IDEA:
# lambda = anonymous (unnamed) function
#
# Syntax:
# lambda argument: expression
#
# Example:
# lambda mage: mage["power"]
# → take a mage dictionary and return its "power"
#
# ============================================================
# DICTIONARY + LAMBDA
# ============================================================
#
# Get a value:
# lambda x: x["power"]
# lambda x: x["name"]
#
# Example:
# mage = {"name": "Gandalf", "power": 95}
# lambda mage: mage["power"]   → 95
#
# ============================================================
# sorted() + lambda
# ============================================================
#
# Sort by dictionary value:
#
# sorted(
#     data,
#     key=lambda x: x["power"],
# )
#
# Descending:
#
# sorted(
#     data,
#     key=lambda x: x["power"],
#     reverse=True,
# )
#
# Remember:
# key=lambda x: WHAT_TO_SORT_BY
#
# ============================================================
# filter() + lambda
# ============================================================
#
# Keep items when condition is TRUE:
#
# list(
#     filter(
#         lambda x: x["power"] >= min_power,
#         data,
#     )
# )
#
# Remember:
# filter = KEEP / REMOVE
#
# lambda must return True or False.
#
# Example:
# 95 >= 80 → True → KEEP
# 60 >= 80 → False → REMOVE
#
# ============================================================
# map() + lambda
# ============================================================
#
# Transform EVERY item:
#
# list(
#     map(
#         lambda x: f"* {x} *",
#         data,
#     )
# )
#
# Remember:
# map = TRANSFORM
#
# Example:
# "fireball" → "* fireball *"
#
# ============================================================
# max() / min() + lambda
# ============================================================
#
# Find dictionary with highest/lowest value:
#
# max(
#     mages,
#     key=lambda mage: mage["power"],
# )
#
# min(
#     mages,
#     key=lambda mage: mage["power"],
# )
#
# If you want the POWER itself:
#
# max(
#     mages,
#     key=lambda mage: mage["power"],
# )["power"]
#
# ============================================================
# sum() + map() + len() → AVERAGE
# ============================================================
#
# Get all powers:
#
# map(lambda mage: mage["power"], mages)
#
# Total:
#
# sum(
#     map(lambda mage: mage["power"], mages)
# )
#
# Average:
#
# sum(
#     map(lambda mage: mage["power"], mages)
# ) / len(mages)
#
# Round to 2 decimals:
#
# round(
#     sum(
#         map(lambda mage: mage["power"], mages)
#     ) / len(mages),
#     2,
# )
#
# ============================================================
# QUICK MEMORY
# ============================================================
#
# sorted → SORT
# filter  → KEEP / REMOVE
# map     → TRANSFORM
# max     → BIGGEST
# min     → SMALLEST
# sum     → TOTAL
# len     → COUNT
# round   → DECIMAL PLACES
#
# ============================================================
# EX0 FUNCTIONS
# ============================================================
#
# artifact_sorter()
# → sorted() + lambda
#
# power_filter()
# → filter() + lambda
#
# spell_transformer()
# → map() + lambda
#
# mage_stats()
# → max() + min() + sum() + map() + len() + round()
#
# ============================================================

def artifact_sorter(
    artifacts: list[dict],
) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(
    mages: list[dict],
    min_power: int,
) -> list[dict]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages,
        )
    )


def spell_transformer(
    spells: list[str],
) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells,
        )
    )


def mage_stats(
    mages: list[dict],
) -> dict:
    max_power = max(
        mages,
        key=lambda mage: mage["power"],
    )["power"]

    min_power = min(
        mages,
        key=lambda mage: mage["power"],
    )["power"]

    avg_power = round(
        sum(
            map(lambda mage: mage["power"], mages)
        ) / len(mages),
        2,
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Ice Wand", "power": 70, "type": "wand"},
    ]

    mages = [
        {"name": "Gandalf", "power": 95, "element": "light"},
        {"name": "Merlin", "power": 80, "element": "arcane"},
        {"name": "Morgana", "power": 60, "element": "dark"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    for artifact in sorted_artifacts:
        print(
            f"{artifact['name']} "
            f"({artifact['power']} power)"
        )

    print("\nTesting power filter...")
    powerful_mages = power_filter(mages, 80)

    for mage in powerful_mages:
        print(
            f"{mage['name']} "
            f"({mage['power']} power)"
        )

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()
