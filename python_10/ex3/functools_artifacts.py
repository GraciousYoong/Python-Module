from collections.abc import Callable
from functools import (
    lru_cache,
    partial,
    reduce,
    singledispatch,
)
from operator import add, mul
from typing import Any


def spell_reducer(
    spells: list[int],
    operation: str,
) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable,
) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(
            base_enchantment,
            50,
            "lightning",
        ),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(spell_data: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def _(spell_data: int) -> str:
        return f"{spell_data} damage"

    @spell.register
    def _(spell_data: str) -> str:
        return spell_data

    @spell.register
    def _(spell_data: list) -> str:
        return f"{len(spell_data)} spells"

    return spell


def base_enchantment(
    power: int,
    element: str,
    target: str,
) -> str:
    return f"{element} {target} ({power} power)"


def main() -> None:
    print("Testing spell reducer...")

    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    enchantments = partial_enchanter(base_enchantment)

    print(enchantments["fire"]("Sword"))
    print(enchantments["ice"]("Shield"))
    print(enchantments["lightning"]("Staff"))

    print("\nTesting memoized fibonacci...")

    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(
        f"Multi-cast: "
        f"{dispatcher(['fireball', 'heal', 'shield'])}"
    )
    print(f"{dispatcher(3.14)}")


if __name__ == "__main__":
    main()
