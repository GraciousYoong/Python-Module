#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print(
            "Usage: ft_stream_management.py <file>",
            file=sys.stderr,
        )
    else:
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")

        file: typing.IO[str]

        try:
            file = open(filename, "r")
        except OSError as error:
            print(
                f"[STDERR] Error opening file '{filename}': {error}",
                file=sys.stderr,
            )
        else:
            content = file.read()
            print("---\n")
            print(content, end="")
            print("\n")
            print("---")
            file.close()
            print(f"File '{filename}' closed.\n")

            lines = content.split("\n")
            transformed = [
                line + "#"
                for line in lines
                if line != ""
            ]

            print("Transform data:")
            print("---\n")
            for line in transformed:
                print(line)
            print("\n---")

            print("Enter new file name (or empty): ", end="", flush=True)
            new_file = sys.stdin.readline().strip()

            if new_file == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file}'")

                out: typing.IO[str]

                try:
                    out = open(new_file, "w")
                except OSError as error:
                    print(
                        f"[STDEER] Error opening file '{new_file}': {error}",
                        file=sys.stderr,
                    )
                    print("Data not saved.")
                else:
                    for line in transformed:
                        out.write(line + "\n")

                    out.close()

                    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    main()
