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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    # Numeric Processor
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"  Trying to validate input '42': {np.validate(42)}")
    print(f"  Trying to validate input 'Hello': {np.validate('Hello')}")

    print("  Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore
    except Exception as e:
        print(f"  Got exception: {e}")

    np.ingest([1, 2, 3, 4, 5])
    print(f"  Processing data: [1, 2, 3, 4, 5]")
    print(f"  Extracting 3 values...")
    for i in range(3):
        rank, value = np.output()
        print(f"  Numeric value {rank}: {value}")

    # Text Processor
    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"  Trying to validate input '42': {tp.validate(42)}")

    tp.ingest(["Hello", "Nexus", "World"])
    print(f"  Processing data: ['Hello', 'Nexus', 'World']")
    print(f"  Extracting 1 value...")
    rank, value = tp.output()
    print(f"  Text value {rank}: {value}")

    # Log Processor
    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"  Trying to validate input 'Hello': {lp.validate('Hello')}")

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]
    lp.ingest(logs)
    print(f"  Processing data: {logs}")
    print(f"  Extracting 2 values...")
    for i in range(2):
        rank, value = lp.output()
        print(f"  Log entry {rank}: {value}")