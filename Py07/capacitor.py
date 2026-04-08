from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(fact: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = fact.create_base()
    evol = fact.create_evolved()
    creature = [base, evol]
    for c in creature:
        if c == base:
            print("base:")
        else:
            print("evolved:")
        print(c.describe())
        print(c.attack())
        print(c.heal('c'))


def test_transform_factory(fact: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = fact.create_base()
    evol = fact.create_evolved()
    creature = [base, evol]
    for c in creature:
        if c == base:
            print("base:")
        else:
            print("evolved:")
        print(c.describe())
        print(c.attack())
        print(c.transform())
        print(c.attack())
        print(c.revert())


if __name__ == "__main__":
    hf = HealingCreatureFactory()
    tf = TransformCreatureFactory()
    test_healing_factory(hf)
    print()
    test_transform_factory(tf)
