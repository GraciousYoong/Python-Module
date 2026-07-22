#!/usr/bin/env python3

import typing
import abc


# ---------------- Base Processor ----------------

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0
        self._processed: int = 0

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
        self._rank += 1

        return self._rank, value

    def remaining(self) -> int:
        return len(self._data)

    def stats(self) -> tuple[int, int]:
        return self._processed, len(self._data)


# ---------------- Numeric Processor ----------------

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
            return

        if isinstance(data, (int, float)):
            self._data.append(str(data))
            self._processed += 1
        else:
            for x in data:
                self._data.append(str(x))
                self._processed += 1


# ---------------- Text Processor ----------------

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
            return

        if isinstance(data, str):
            self._data.append(data)
            self._processed += 1
        else:
            for x in data:
                self._data.append(x)
                self._processed += 1


# ---------------- Log Processor ----------------

class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return self._valid_dict(data)

        if isinstance(data, list):
            return all(self._valid_dict(x) for x in data)

        return False

    def _valid_dict(self, data: typing.Any) -> bool:
        if not isinstance(data, dict):
            return False
        return all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def ingest(
        self,
        data: dict[str, str]
        | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            return

        def fmt(d: dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, dict):
            self._data.append(fmt(data))
            self._processed += 1
        else:
            for x in data:
                self._data.append(fmt(x))
                self._processed += 1


# ---------------- DataStream ----------------

class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process "
                      f"element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        for proc in self._processors:
            processed, remaining = proc.stats()
            name = proc.__class__.__name__
            print(
                f"{name}: total {processed} items processed, "
                f"remaining {remaining} on processor"
            )


# ---------------- Test Scenario ----------------

def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    stream = DataStream()

    print("Initialize Data Stream...")
    stream.print_processors_stats()

    print("\n")
    print("Registering Numeric Processor")
    stream.register_processor(NumericProcessor())

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
                "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("\n")
    print(
        "Send first batch of data on stream:",
        batch,
    )

    stream.process_stream(batch)

    stream.print_processors_stats()

    print("\n")
    print("Registering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(batch)

    stream.print_processors_stats()

    print("\n")
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
        )

    # consume demo
    for _ in range(3):
        stream._processors[0].output()

    for _ in range(2):
        stream._processors[1].output()

    for _ in range(1):
        stream._processors[2].output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
