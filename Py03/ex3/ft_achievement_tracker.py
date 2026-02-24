def achivement_hunter() -> None:
    print("=== Achivement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    all_player = [alice, bob, charlie]
    unique = set.union(*all_player)
    common = set.intersection(*all_player)
    only_alice = alice.difference(bob.union(charlie))
    only_bob = bob.difference(alice.union(charlie))
    only_charlie = charlie.difference(alice.union(bob))
    rare_achivement = only_alice.union(only_bob, only_charlie)
    alice_bob_common = bob.intersection(alice)
    alice_unique = alice - bob
    bob_unique = bob - alice
    print(f"alice achievement: {alice}")
    print(f"bob achievement: {bob}")
    print(f"charlie achievement: {charlie}\n")
    print("=== Achievement Analytics ===")
    print(f"All unique achievement: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")
    print(f"Common to all player: {common}")
    print(f"Rare achievements (1 player): {rare_achivement}\n")
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"ALice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    achivement_hunter()
