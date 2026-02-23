class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def watering_plants(plant_list: list):
    print("Open watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise WaterError(f"Cannot water {plant}- invalid plant")
            print(f"watering {plant}")
    except WaterError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    valid = ["tomato", "lettuce", "carrots"]
    invalid = ["tomato", None, "lettuce"]
    print("Testing normal watering...")
    watering_plants(valid)
    print("watering completed\n")
    print("Testing with errors...\n")
    watering_plants(invalid)
    print("\n")
    print("Cleanup always happens, even with errors!")


test_watering_system()
