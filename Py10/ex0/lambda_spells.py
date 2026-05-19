heroes = [
    {"name": "Goku",    "power": 9000, "type": "fighter"},
    {"name": "Saitama", "power": 9999, "type": "fighter"},
    {"name": "Naruto",  "power": 7500, "type": "ninja"},
    {"name": "Levi",    "power": 6800, "type": "soldier"},
    {"name": "Itachi",  "power": 8200, "type": "ninja"},
]

spells = ["Fireball", "Frostbolt", "Thunder", "Shadow Strike", "Holy Light"]
students = {"Alice": 88, "Bob": 72, "Clara": 95}


def artifact_sorter(artifact: list[dict]) -> list[dict]:
    result = sorted(artifact, key=lambda a: a["power"], reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = list(filter(lambda m: m['power'] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda s: "* " +s+ "* ", spells))
    return result


def mages_stats(mages: list[dict]) -> dict:
    stats = {}
    max_pwr = max(mages, key=lambda m: m['power'])
    min_pwr = min(mages, key=lambda m: m['power'])
    total_pwr = list(map(lambda m: m["power"], mages))
    total = sum(total_pwr)
    avg_power = total / len(mages)
    max_pwr_value = max_pwr["power"]
    min_pwr_value = min_pwr["power"]
    stats.update({"max_power":max_pwr_value})
    stats.update({"min_power":min_pwr_value})
    stats.update({"avg_power":avg_power})
    return stats


if __name__ == "__main__":
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Shadow Blade", "power": 78, "type": "weapon"},
    ]
    mages = [
        {"name": "Alex", "power": 95, "element": "fire"},
        {"name": "Jordan", "power": 60, "element": "ice"},
        {"name": "Riley", "power": 80, "element": "lightning"},
    ]
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before {sorted_artifacts[1]['name']}"
        f" ({sorted_artifacts[1]['power']} power)"
    )
    print("\nTesting power filter...")
    filtered = power_filter(mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in filtered]}")
    print("\nTesting spell transformer...")
    transformed = spell_transformer(["fireball", "heal", "shield"])
    print(" ".join(transformed))
    print("\nTesting mage stats...")
    stats = mages_stats(mages)
    print(
        f"Max: {stats['max_power']}, Min: {stats['min_power']},"
        f" Avg: {stats['avg_power']}"
    )