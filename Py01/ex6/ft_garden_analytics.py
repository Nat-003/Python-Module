class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height >= 0:
            self._height = height
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Security: Negative age rejected")

    def grow(self):
        new_height = self.get_height() + 1
        self.set_height(new_height)
        print(f"{self.name} grew 1 cm")

    def get_type(self):
        return "regular"

    def __str__(self):
        return f"{self.name}: {self.get_height()}cm "


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, is_blooming):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def is_flower_blooming(self):
        if self.is_blooming == True:
            return "blooming"
        else:
            return "This flower is not yet blooming"
        
    def get_type(self):
        return "flowering"
    
    def __str__(self):
        base = super().__str__()
        bloom = self.is_flower_blooming()
        return base + f"{self.color} flower ({bloom}) "

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, is_blooming, prize_point):
        super().__init__(name, height, age, color, is_blooming)
        self._prize_point = 0
        self.set_prize_point(prize_point)

    def set_prize_point(self, prize_point):
        if prize_point >= 0:
            self._prize_point = prize_point
        else:
            print("invalid number")

    def get_prize_point(self):
        return self._prize_point
    
    def get_type(self):
        return "prize"
    
    def __str__(self):
        base = super().__str__()
        return base + f"Prize point: {self.get_prize_point()} "
    
class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []
        self.plants_added = 0
        self.total_growth = 0

    def add_plant(self, plant):
        
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.name}'s garden")
        

    def grow_all_plants(self):
        print(f"{self.name} is helping all plants grow...\n")
        for p in self.plants:
            p.grow()
            self.total_growth += 1
        print("\n")

    def garden_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print(f"Plant in {self.name}'s garden")
        for plant in self.plants:
            print(f"{plant}")
        print(f"Plants added: {self.plants_added}, total growth: {self.total_growth}cm")

class GardenManager:
    def __init__(self):
        self.gardens = []
        self.total_garden = 0
    
    @classmethod
    def create_network(cls,gardens):
        manager = cls()
        for g in gardens:
            manager.add_garden(g)
        return manager

    class GardenStat:
        def __init__(self,garden):
            self.garden = garden
        
        def count_plant_types(self):
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.garden.plants:
                plant_type  = plant.get_type()
                if plant_type == "prize":
                    prize +=1
                elif plant_type == "flowering":
                    flowering += 1
                elif plant_type == "regular":
                    regular +=1
            return regular, flowering, prize

        def calculate_score(self):
            score = 0
            for plant in self.garden.plants:
                plant_type  = plant.get_type()
                if plant_type == "prize":
                    score = score + plant.get_prize_point()
            return score

        @staticmethod
        def validate_height_test(plants: list) -> bool:
            for plant in plants:
                if plant.get_height() < 0:
                    return False
            return True

    def add_garden(self,garden):
        self.gardens.append(garden)
        self.total_garden += 1
      
    def garden_report(self,garden):
        stats = self.GardenStat(garden)
        print("\n")
        regular, flowering, prize = stats.count_plant_types()
        print(f"=== {garden.name}'s Garden Report ===")
        print(f"Plant in {garden.name}'s garden")
        print(f"Plants added: {garden.plants_added}, total growth: {garden.total_growth}cm")
        print(f"Plant types: {regular} Regular, {flowering} Flowering, {prize} Prize Flower")
        print("\n")

    def users_score(self):
        for g in self.gardens:
            stats = self.GardenStat(g)
            score = stats.calculate_score()
            print(f"{g.name}'s score: {score}")



if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    
    # Setup plants
    oak = Plant("Oak Tree", 100, 10)
    rose = FloweringPlant("Rose", 25, 1, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 1, "yellow", True, 10)

    pine = Plant("Evergreen Pine", 150, 20)
    lavender = FloweringPlant("Lavender", 30, 2, "purple", False)
    orchid = PrizeFlower("Silver Orchid", 45, 4, "silver", True, 25)

    # Setup Garden
    alice_garden = Garden("Alice")
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Grow phase
    alice_garden.grow_all_plants()

    # Create another garden for a different user
    bob_garden = Garden("Bob")
    bob_garden.add_plant(pine)
    bob_garden.add_plant(lavender)
    bob_garden.add_plant(orchid)

    # Update the network to include both Alice and Bob
    garden_list = [alice_garden, bob_garden]
    manager = GardenManager.create_network(garden_list)

    # Report
    manager.garden_report(alice_garden)
    manager.garden_report(bob_garden)
    # Validation & Score
    my_plants = [pine,rose]
    is_valid = GardenManager.GardenStat.validate_height_test(my_plants)
    manager.users_score()
    print("\n")
    print(f"height validation test: {is_valid}")
    print(f"Total garden managed: {manager.total_garden}")