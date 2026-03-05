
raw_scores = [2300, 1800, 2150, 1900, 2500, 1800]


player_data = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 2500
}


earned_achievements = [
    "first_kill", "level_10", "first_kill",
    "boss_slayer", "level_10", "speed_demon"
]


def list_test(player_data: dict) -> list:
    high_scorers = [name for name, score in player_data.items()
                    if score > 2000]
    scores_doubled = [score * 2 for score in player_data.values()]
    active_player = [name for name in player_data.keys()]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_player}")


# def dick_test(player_data: dict) -> None:



if __name__ == "__main__":
    list_test(player_data)
