#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
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
            print(f"File '{filename}' closed.\n")

            # transform
            lines = content.split("\n")
            transformed = [
                line + "#" for line in lines if line != ""
            ]

            print("Transform data:")
            print("---\n")
            for line in transformed:
                print(line)
            print("\n")
            print("---")

            new_file = input("Enter new file name (or empty): ")

            if len(new_file) == 0:
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file}'")

                out: typing.IO[str] = open(new_file, "w")

                for line in transformed:
                    out.write(line + "\n")

                out.close()

                print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    main()
