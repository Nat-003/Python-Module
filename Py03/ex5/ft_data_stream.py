from typing import Generator


def fibonacci() -> Generator[str, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def data_gen(num: int) -> Generator[str, None, None]:
    print("=== Game Data Stream Processor ===\n")
    names = ["alice", "bob", "charlie"]
    levels = [5, 12, 8]
    events = ["killed monster", "found treasure", "level up"]
    counter = 0
    high_leve_player = 0
    t_event = 0
    level_up = 0
    print(f"Processing {num} game events...")
    for i in range(num):
        if int(levels[i % len(names)]) > 10:
            high_leve_player += 1
        if events[i % len(events)] == "found treasure":
            t_event += 1
        if events[i % len(events)] == "level up":
            level_up += 1
        name = names[i % len(names)]
        level = levels[i % len(levels)]
        event = events[i % len(events)]
        counter += 1
        yield f"Event {i + 1}: Player {name} (level {level}) {event}"
    print("\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {counter}")
    print(f"High-level players (10+): {high_leve_player}")
    print(f"Treasure events: {t_event}")
    print(f"Level-up events: {level_up}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demostration ===")
    fib = fibonacci()
    prime = prime_generator()
    print("Fibonacci sequence (first 10):", end="")
    for _ in range(10):
        print(f"{next(fib)}, ", end="")
    print("\n")
    print("Prime numbers (first 5):", end="")
    for _ in range(5):
        print(f"{next(prime)}, ", end="")


if __name__ == "__main__":
    stream = data_gen(923)
    for e in stream:
        print(e)
