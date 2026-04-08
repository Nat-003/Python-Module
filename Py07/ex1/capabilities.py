from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.state = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip"

    def heal(self, target: str) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance"

    def heal(self, target: str) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.state:
            return f"{self.name} performed a boosted strike"
        else:
            return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.state = True
        return f"{self.name} shifts into a sharper form"

    def revert(self) -> str:
        self.state = False
        return f"{self.name} returns to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.state:
            return f"{self.name} unleashes a devastating morph strike"
        else:
            return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.state = True
        return f"{self.name} morph into a dragonic battle form"

    def revert(self) -> str:
        self.state = False
        return f"{self.name} stabilizes its form"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
