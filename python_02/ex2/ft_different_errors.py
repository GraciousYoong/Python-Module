def garden_operations(operation_number: int):
    if operation_number == 0:
        # ValueError
        int("abc")
    elif operation_number == 1:
        # ZeroDivisionError
        return 10 / 0
    elif operation_number == 2:
        # FileNotFoundError
        open("/non/existent/file", "r")
    elif operation_number == 3:
        # TypeError
        return "temperature: " + 25
    else:
        return "Operation completed successfully"


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            result = garden_operations(i)
            if result is not None:
                print(result)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
