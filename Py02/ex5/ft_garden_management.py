class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant: str):
        if plant.name == "":
            raise PlantError("Name cannot be empty")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def watering_plants(self):
        print("Open watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError(f"Cannot water {plant.name}- invalid plant")
                print(f"watering {plant.name}")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        for plant in self.plants:
            if plant.water < 1 or plant.water > 10:
                raise WaterError(f"Error: checking {plant.name}: Water level {plant.water}outside range(2,12)")
            if plant.sun < 2 or plant.sun > 12:
                raise ValueError(f"Error: checking {plant.name}: Sunlight hours {plant.sun} outside range(2,12)")
            print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")
        print("Test completd")


warden = GardenManager()
rose = Plant("rose", 5, 7)
sunflower = Plant("Sunflower", 2, 8)
orchide = Plant("", 6, 7)
sabot = Plant("Sabot de Venus", 5, 15)
plants_list = [rose, sunflower, sabot, orchide]


def test_garden_management():
    print("=== Garden Management System === \n")
    print("Adding plants to garden...")
    try:
        for plant in plants_list:
            warden.add_plant(plant)
    except PlantError as e:
        print(f"{e}")
    print("\n")
    print("Watering plants...")
    try:
        warden.watering_plants()
    except WaterError as e:
        print(f"{e}")
    print("\n")
    print("Checking plant health...")
    try:
        warden.check_plant_health()
    except (WaterError, ValueError) as e:
        print(f"{e}")


test_garden_management()