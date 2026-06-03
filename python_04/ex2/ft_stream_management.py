#!/usr/bin/env python3

import typing
import sys


def read_line() -> str:
    buffer = ""

    while True:
        char = sys.stdin.read(1)

        if char == "":
            break

        if char == "\n":
            break

        buffer += char

    return buffer


print("=== Cyber Archives Recovery & Preservation ===")

filename = sys.argv[1] if len(sys.argv) > 1 else ""

if len(filename) == 0:
    print("Usage: ft_stream_management.py <file>")
else:
    print(f"Accessing file '{filename}'")

    file: typing.IO[str]

    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{filename}': {error}")
    else:
        content = file.read()
        file.close()

        print("---")
        print(content, end="")
        print("---")
        print(f"File '{filename}' closed.")

        lines = content.split("\n")
        transformed = [
            line + "#" for line in lines if line != ""
        ]

        print("Transform data:")
        print("---")
        for line in transformed:
            print(line)
        print("---")

        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()

        new_file = read_line()

        if len(new_file) == 0:
            print("Data not saved.")
        else:
            print(f"Saving data to '{new_file}'")

            try:
                out: typing.IO[str] = open(new_file, "w")

                for line in transformed:
                    out.write(line + "\n")

                out.flush()
                out.close()

            except OSError as error:
                print(
                    f"[STDERR] Error opening file '{new_file}': {error}"
                )
                print("Data not saved.")
