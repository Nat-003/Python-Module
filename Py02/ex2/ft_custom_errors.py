class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_water_level(num):
    if num < 5:
        raise WaterError("Not enough water")


def check_wilting(is_wilting):
    if is_wilting:
        raise PlantError("The tomato plant is wilting")


def test_errors():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_wilting(True)
    except PlantError as e:
        print(f"Caught a PlantError: {e}\n")

    print("Testing Water Error...")
    try:
        check_water_level(2)
    except WaterError as e:
        print(f"Caught a WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_water_level(1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_wilting(True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


test_errors()
