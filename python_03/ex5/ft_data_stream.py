#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()

    i = 0
    while i < 1000:
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")
        i += 1

    event_list: list[tuple[str, str]] = []

    j = 0
    while j < 10:
        event_list.append(next(event_gen))
        j += 1

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
