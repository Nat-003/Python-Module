from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self):
        super().__init__()
        self.stored_data = []
        self.counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.stored_data) == 0:
            raise ValueError("No data to output")
        data = self.stored_data.pop(0)
        return data


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        elif isinstance(data, (int, float)):
            return True
        elif isinstance(data, list) and all(isinstance(item, (int ,float)) for item in data):
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError(f"wrong data entered: not an int,float or list")
        elif isinstance(data, list):
            for d in data:
                    tuple_data = (self.counter, str(d))
                    self.stored_data.append(tuple_data)
                    self.counter += 1
        else:
            tuple_data = (self.counter, str(data))
            self.stored_data.append(tuple_data)
            self.counter += 1

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list) and all(isinstance(item, str) for item in data):
            return True
        else:
            return False
    
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError(f"wrong data entered: not an str")
        elif isinstance(data, list):
            for s in data:
                tuple_data = (self.counter, s)
                self.stored_data.append(tuple_data)
                self.counter += 1
        else:
            tuple_data = (self.counter, data)
            self.stored_data.append(tuple_data)
            self.counter += 1

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and all(isinstance(key, str) for key in data.keys()) and all(isinstance(value, str) for value in data.values()):
            return True
        elif isinstance(data, list) and all(
            isinstance(item, dict)
            and all(isinstance(key, str) for key in item.keys())
            and all(isinstance(value, str) for value in item.values())
            for item in data):
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError(f"wrong data entered: not an dict")
        elif isinstance(data, list):
            for di in data:
                val = ": ".join(di.values())
                tuple_data = (self.counter, val)
                self.stored_data.append(tuple_data)
                self.counter += 1
        else:
            val = ": ".join(data.values())
            tuple_data = (self.counter, val)
            self.stored_data.append(tuple_data)
            self.counter += 1

class DataStream:
    def __init__(self):
        self.processor = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for e in stream:
            for proc in self.processor:
                if proc.validate(e):
                    proc.ingest(e)
                    break
            else:
                print(f"DataStream error - Can't process element in stream: {e}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processor:
            print("No processor found, no data")
        else:
            for proc in self.processor:
                name = type(proc).__name__
                total = proc.counter
                remaining = len(proc.stored_data)
                print(f"{name}: total {total} items processed, remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    ds.register_processor(NumericProcessor())

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42,
        ["Hi", "five"]
    ]

    print(f"\nSend first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("\nSend the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for proc in ds.processor:
        name = type(proc).__name__
        if "Numeric" in name:
            for _ in range(3):
                proc.output()
        elif "Text" in name:
            for _ in range(2):
                proc.output()
        elif "Log" in name:
            proc.output()
    ds.print_processors_stats()