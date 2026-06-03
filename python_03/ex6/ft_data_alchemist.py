#!/usr/bin/env python3

import random


print("=== Game Data Alchemist ===")

players = [
    "Alice", "bob", "Charlie", "dylan",
    "Emma", "Gregory", "john", "kevin", "Liam"
]

print(f"Initial list of players: {players}")

capitalized_all = [name.capitalize() for name in players]
print(
    f"New list with all names capitalized: "
    f"{capitalized_all}"
)

capitalized_only = [
    name for name in capitalized_all
    if name == name.capitalize()
]

print(
    f"New list of capitalized names only: "
    f"{capitalized_only}"
)

score_dict = {
    name: random.randint(50, 1000)
    for name in capitalized_all
}

print(f"Score dict: {score_dict}")

average_score = sum(score_dict.values()) / len(score_dict)
print(f"Score average is {round(average_score, 2)}")

high_scores = {
    name: score
    for name, score in score_dict.items()
    if score > average_score
}

print(f"High scores: {high_scores}")
