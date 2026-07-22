#!/usr/bin/env python3

import typing
import abc


# ---------------- Export Plugin (Protocol) ----------------

class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


# ---------------- Base Processor ----------------

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
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
        rank = self._processed
        self._processed += 1

        return rank, value

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

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            return

        if isinstance(data, (int, float)):
            self._data.append(str(data))
        else:
            for x in data:
                self._data.append(str(x))


# ---------------- Text Processor ----------------

class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            return

        if isinstance(data, str):
            self._data.append(data)
        else:
            for x in data:
                self._data.append(x)


# ---------------- Log Processor ----------------

class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return self._valid(data)
        if isinstance(data, list):
            return all(self._valid(x) for x in data)
        return False

    def _valid(self, data: typing.Any) -> bool:
        if not isinstance(data, dict):
            return False
        return all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in data.items()
        )

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            return

        def fmt(d: dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, dict):
            self._data.append(fmt(data))
        else:
            for x in data:
                self._data.append(fmt(x))


# ---------------- CSV Plugin ----------------

class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [item[1] for item in data]
        print(",".join(values))


# ---------------- JSON Plugin ----------------

class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")

        items: list[str] = []
        i = 0

        for _, value in data:
            items.append(f"\"item_{i}\": \"{value}\"")
            i += 1

        print("{" + ", ".join(items) + "}")


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
                print(f"DataStream error - Can't "
                      f"process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        for proc in self._processors:
            processed, remaining = proc.stats()
            print(
                f"{proc.__class__.__name__}: "
                f"total {processed} items processed, "
                f"remaining {remaining} on processor"
            )

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin,
    ) -> None:
        for _ in range(nb):
            batch: list[tuple[int, str]] = []

            for proc in self._processors:
                rank, value = proc.output()
                if rank != -1:
                    batch.append((rank, value))

            plugin.process_output(batch)


# ---------------- Demo ----------------

def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()

    print("Initialize Data Stream...")
    stream.print_processors_stats()

    print("Registering Processors")

    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
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

    print("Send first batch of data on stream:", batch1)
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())

    stream.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR",
                "log_message": "500 server crash"},
            {"log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send another batch of data:", batch2)
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
