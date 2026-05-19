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


def power_validator(min_validator: int) -> Callable:
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0] if isinstance(args[0], int) else args[2]
            if power >= min_validator:
                result = func(*args, **kwargs)
                return result
            else:
                return "insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(
                        f"Spell failed, retrying "
                        f"(attempt {attempt + 1}/{max_attempts})"
                        )
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"
    

if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        import time
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball("Dragon", 50)
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception("Spell unstable!")

    print(unstable_spell())
    print("\nWaaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
