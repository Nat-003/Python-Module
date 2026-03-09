
player_data = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 2050
}


earned_achievements = [
    "first_kill", "level_10", "first_kill",
    "boss_slayer", "level_10", "speed_demon"
]


def list_test(player_data: dict) -> None:
    print("=== List Coprehension Exemples ===")
    high_scorers = [name for name, score in player_data.items()
                    if score > 2000]
    scores_doubled = [score * 2 for score in player_data.values()]
    active_player = [name for name in player_data.keys()]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_player}")


def dick_test(player_data: dict) -> dict:
    print("=== Dict Comprehension Exemples ===")
    print(f"Player Scores: {player_data}")
    score_categories = {
        name: ("High" if score > 2000
               else "Medium" if score >= 1500 else "Low")
        for name, score in player_data.items()
        }
    achievement_counts = {name: len(name) for name in player_data.keys()}
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")
    return achievement_counts


def set_test(player_data: dict, achievements: list) -> set:
    u_players = {name for name in player_data.keys()}
    u_achievements = {ach for ach in achievements}
    raw_regions = ["north", "east", "central", "north"]
    active_regions = {r for r in raw_regions}
    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {u_players}")
    print(f"Unique achievements: {u_achievements}")
    print(f"Active regions: {active_regions}")
    return u_achievements


def combined_analysis(player_data: dict, unique_achievements: set,
                      achievement_counts: dict) -> None:
    total_players = len(player_data)
    total_unique = len(unique_achievements)
    avg_score = sum(player_data.values()) / total_players
    top_name = max(player_data, key=player_data.get)
    top_score = player_data[top_name]
    top_achievements = achievement_counts.get(top_name, 0)

    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_name} ({top_score} points,"
          f"{top_achievements} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    list_test(player_data)
    print("\n")
    achievement_counts = dick_test(player_data)
    print("\n")
    unique_achievements = set_test(player_data, earned_achievements)
    print("\n")
    combined_analysis(player_data, unique_achievements, achievement_counts)
