#!/usr/bin/env python3


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return True, data

        with open(filename, "w") as file:
            file.write(content)
            return True, "Content successfully written to file"

    except OSError as error:
        return False, str(error)


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print("\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print("\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "read"))
    print("\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(
        secure_archive(
            "new_archive.txt",
            "write",
            "[FRAGMENT TEST] Data preserved successfully\n",
        )
    )


if __name__ == "__main__":
    main()
