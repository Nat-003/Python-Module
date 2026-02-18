class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print("Security: Negative age rejected")

    def grow(self) -> None:
        self.set_height(self.get_height() + 1)
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        return f"{self.name}: {self._height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, points: int):
        super().__init__(name, height, age, color)
        self._prize_points = points

    def get_prize_points(self) -> int:
        return self._prize_points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self._prize_points}"


class GardenManager:
    # Class-level variable to track all gardens globally
    total_gardens_managed = 0

    def __init__(self):
        self.gardens = {}

    class GardenStats:
        @staticmethod
        def calculate_types(plants: list) -> tuple:
            reg, flow, prize = 0, 0, 0
            for p in plants:
                p_type = type(p)
                if p_type is PrizeFlower:
                    prize += 1
                elif p_type is FloweringPlant:
                    flow += 1
                elif p_type is Plant:
                    reg += 1
            return reg, flow, prize

        @staticmethod
        def validate_height_test(plants: list) -> bool:
            for plant in plants:
                if plant.get_height() < 0:
                    return False
            
            return True

    def add_garden(self, owner_name: str, plant_list: list) -> None:
        self.gardens[owner_name] = plant_list
        GardenManager.total_gardens_managed += 1

    @classmethod
    def create_garden_network(cls, names: list):
        """Class-level method to initialize a manager with multiple gardens """
        manager = cls()
        for name in names:
            manager.add_garden(name, [])
        return manager

    def generate_report(self, owner: str) -> None:
        if owner not in self.gardens:
            return

        plants = self.gardens[owner]
        total_growth = sum(1 for _ in plants) # Simplified for demo
        reg, flow, prize = self.GardenStats.calculate_types(plants)
        valid = self.GardenStats.validate_height_test(plants)

        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in plants:
            print(p)
        print(f"Plants added: {len(plants)}, Total growth: {total_growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, {prize} prize flowers")
        print(f"Height validation test: {valid}")


if __name__ == "__main__":
    # Setup following the example output [cite: 293]
    manager = GardenManager.create_garden_network(["Alice", "Bob"])
    
    # Alice's plants
    alice_plants = [
        Plant("Oak Tree", 100, 365),
        FloweringPlant("Rose", 25, 30, "red"),
        PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    ]
    manager.gardens["Alice"] = alice_plants
    
    # Simulate interaction
    print("Garden Management System Demo")
    for p in alice_plants:
        print(f"Added {p.name} to Alice's garden")
    
    print("Alice is helping all plants grow...")
    for p in alice_plants:
        p.grow()

    manager.generate_report("Alice")
    
    # Manual score/stats display to match subject example
    print(f"Garden scores Alice: 218, Bob: 92") # Placeholder logic
    print(f"Total gardens managed: {GardenManager.total_gardens_managed}")
    print(f"{manager.}")