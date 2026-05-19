# students = [("Alice", 88), ("Bob", 72), ("Clara", 95)]
# result = sorted(students, key=lambda s: s[1],reverse=True)
# print(result)

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
    result = list(map(lambda s: "*"+s+"*", spells))
    return result


def mages_stats(mages: list[dict]) -> dict:
    stats = {}
    max_pwr = max(mages, key=lambda m: m['power'])
    min_pwr = min(mages, key=lambda m: m['power'])
    total_pwr = list(map(lambda m: m["power"], mages))
    total = sum(total_pwr)
    average_pwr = total / len(mages)
    max_pwr_value = max_pwr["power"]
    min_pwr_value = min_pwr["power"]
    stats.update({"max_power":max_pwr_value})
    stats.update({"min_power":min_pwr_value})
    stats.update({"average_power":average_pwr})
    return stats


# artifact_sorter(heroes)
# power = power_filter(heroes, 9000)
# print(power)
# print(spell_transformer(spells))
print(mages_stats(heroes))
if __name__ == "__main__":
