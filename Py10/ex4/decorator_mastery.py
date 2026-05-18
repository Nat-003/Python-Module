from typing import Callable
import time
import functools


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


@spell_timer
def hello():
    print("Hello")


def power_validator(min_validator: int) -> Callable:
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] >= min_validator:
                result = func(*args, **kwargs)
                return result
            else:
                return "insufficient power for this spell"
        return wrapper
    return decorator

if __name__ == "__main__":
    hello()