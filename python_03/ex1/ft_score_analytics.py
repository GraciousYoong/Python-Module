#!/usr/bin/env python3

import sys


print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )
else:
    scores = []

    index = 1
    while index < len(sys.argv):
        try:
            score = int(sys.argv[index])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[index]}'")
        index += 1

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        total_score = sum(scores)
        average_score = total_score / len(scores)
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
