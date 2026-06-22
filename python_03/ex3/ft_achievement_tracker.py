#!/usr/bin/env python3

import random


def gen_player_achievements() -> set[str]:
    achievements = {
        "First Steps",
        "Speed Runner",
        "Treasure Hunter",
        "Master Explorer",
        "Collector Supreme",
        "Boss Slayer",
        "Crafting Genius",
        "Sharp Mind",
        "Strategist",
        "Survivor",
        "Untouchable",
        "World Savior",
        "Hidden Path Finder",
        "Unstoppable",
    }

    count = random.randint(5, 10)
    return set(random.sample(list(achievements), count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = alice.union(
        bob,
        charlie,
        dylan
    )

    common_achievements = alice.intersection(
        bob,
        charlie,
        dylan
    )

    print(f"All distinct achievements: {all_achievements}")
    print(f"Common achievements: {common_achievements}")

    alice_only = alice.difference(
        bob.union(charlie, dylan)
    )
    bob_only = bob.difference(
        alice.union(charlie, dylan)
    )
    charlie_only = charlie.difference(
        alice.union(bob, dylan)
    )
    dylan_only = dylan.difference(
        alice.union(bob, charlie)
    )

    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}")

    print(
        f"Alice is missing: "
        f"{all_achievements.difference(alice)}"
    )
    print(
        f"Bob is missing: "
        f"{all_achievements.difference(bob)}"
    )
    print(
        f"Charlie is missing: "
        f"{all_achievements.difference(charlie)}"
    )
    print(
        f"Dylan is missing: "
        f"{all_achievements.difference(dylan)}"
    )


if __name__ == "__main__":
    main()
