from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, BattleError
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: list[tuple]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fact1, strat1 = opponents[i]
            fact2, strat2 = opponents[j]
            creature1 = fact1.create_base()
            creature2 = fact2.create_base()
            print("* Battle *")
            print(creature1.describe())
            print("vs")
            print(creature2.describe())
            print("now fight!")
            try:
                strat1.act(creature1)
                strat2.act(creature2)
            except BattleError as e:
                print(f"Battle error, aborting tournament: {e}")

if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()
    hf = HealingCreatureFactory()
    tf = TransformCreatureFactory()

    ns = NormalStrategy()
    ag = AggressiveStrategy()
    df = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    battle([(ff, ns), (hf, df)])

    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    battle([(ff, ag), (hf, df)])

    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved")
    battle([(af, ns), (hf, df), (tf, ag)])
