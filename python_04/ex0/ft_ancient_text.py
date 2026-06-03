#!/usr/bin/env python3

import sys
import typing


print("=== Cyber Archives Recovery ===")


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")

    file: typing.IO[str]

    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
    else:
        content = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
