#!/usr/bin/env python3

import sys
import typing


def main() -> None:
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
            print("---\n")
            print(content, end="")
            print("\n")
            print("---")
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()

# file example:
# file name:
# ancient_fragment.txt
# content:
# [FRAGMENT 001] Digital preservation protocols established 2087
# [FRAGMENT 002] Knowledge must survive the entropy wars
# [FRAGMENT 003] Every byte saved is a victory against oblivion
