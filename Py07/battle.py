from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    creatures = [base, evolved]
    for c in creatures:
        print(c.describe())
        print(c.attack())


def battle(fact1: CreatureFactory, fact2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = fact1.create_base()
    base2 = fact2.create_base()
    print(f"{base1.describe()} vs {base2.describe()}")
    print("fight")
    print(f"{base1.attack()}")
    print(f"{base2.attack()}")


if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()
    test_factory(ff)
    print("\n")
    test_factory(af)
    print("\n")
    battle(ff, af)
