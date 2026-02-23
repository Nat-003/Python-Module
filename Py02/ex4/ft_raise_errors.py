def check_name(plant_name: str):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty")


def check_water(water_level: int):
    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} outside the range (1,10)")


def check_sunlight(sunlight_hours: int):
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}(2,12)")


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    check_name(plant_name)
    check_water(water_level)
    check_sunlight(sunlight_hours)
    print(f"Plant '{plant_name}' is healthy\n")


def test_plant_checks():
    print("=== Garden Plant Health Checker\n")
    print("Testing with good vales...")
    try:
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 45, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\n")
    print("All error raising tests completed!")


test_plant_checks()
