import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 2:
        arg_list = []
        try:
            for arg in sys.argv[1:]:
                value = int(arg)
                arg_list.append(value)
            print(arg_list)
            print(f"Total Player: {len(arg_list)}")
            print(f"Total Score: {sum(arg_list)}")
            print(f"Average Score: {sum(arg_list) / len(arg_list)}")
            print(f"High Score: {max(arg_list)}")
            print(f"Low Score: {min(arg_list)}")
            print(f"Score Range: {max(arg_list) - min(arg_list)}")
        except ValueError:
            print("Error: All argument must be integers")
    else:
        print("No scores provided. Usage: python3 ft_score_analyticsa.py "
              "<score1> <score2>")


if __name__ == "__main__":
    score_analytics()
