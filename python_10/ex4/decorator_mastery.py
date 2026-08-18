import time
from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    """Measure and print the execution time of a spell."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Create a decorator that checks the spell's power."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, spell_name: str, power: int):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Create a decorator that retries a failed spell."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:
    """Represent a guild of mages."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check whether a mage name is valid."""
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if the mage has enough power."""
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Cast a fireball spell."""
    print("Casting fireball...")
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def failed_spell() -> str:
    """A spell that always fails."""
    raise Exception("Spell failed")


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    print(failed_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
