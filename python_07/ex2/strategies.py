import abc
import typing
from ex0.creatures import Creature
from ex1.capabilities import (
    HealCapability,
    TransformCapability,
)


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError("Invalid strategy-Creature combination")

        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f'Invalid Creature "{creature.name}" '
                "for this aggressive strategy"
            )
        capability = typing.cast(TransformCapability, creature)
        print(capability.transform())
        print(creature.attack())
        print(capability.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f'Invalid Creature "{creature.name}" '
                "for this defensive strategy"
            )

        capability = typing.cast(HealCapability, creature)
        print(creature.attack())
        print(capability.heal())
