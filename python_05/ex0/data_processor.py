#!/usr/bin/env python3

import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            return -1, ""

        value = self._data.pop(0)
        rank = self._rank
        self._rank += 1

        return rank, value


# ---------------- Numeric ----------------

class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)

        return False

    def ingest(
        self,
        data: int | float | list[int | float],
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, (int, float)):
            self._data.append(str(data))
        else:
            for x in data:
                self._data.append(str(x))


# ---------------- Text ----------------

class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)

        return False

    def ingest(
        self,
        data: str | list[str],
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, str):
            self._data.append(data)
        else:
            for x in data:
                self._data.append(x)


# ---------------- Log ----------------

class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )

        return False

    def ingest(
        self,
        data: dict[str, str]
        | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, dict):
            self._data.append(format_log(data))
        else:
            for item in data:
                self._data.append(format_log(item))


# ---------------- Testing ----------------

def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    # ---------------- Numeric ----------------
    print("Testing Numeric Processor...")
    num = NumericProcessor()

    print("Trying to validate input '42':", num.validate(42))
    print("Trying to validate input 'Hello':", num.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    i = 0
    while i < 3:
        rank, value = num.output()
        print(f"Numeric value {rank}: {value}")
        i += 1

    # ---------------- Text ----------------
    print("\n")
    print("Testing Text Processor...")
    text = TextProcessor()

    print("Trying to validate input '42':", text.validate(42))

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    # ---------------- Log ----------------
    print("\n")
    print("Testing Log Processor...")
    log = LogProcessor()

    print("Trying to validate input 'Hello':", log.validate("Hello"))

    print(
        "Processing data: [{'log_level': 'NOTICE', "
        "'log_message': 'Connection to server'}, "
        "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
    )

    log.ingest(
        [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
        ]
    )

    print("Extracting 2 values...")
    i = 0
    while i < 2:
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")
        i += 1


if __name__ == "__main__":
    main()
