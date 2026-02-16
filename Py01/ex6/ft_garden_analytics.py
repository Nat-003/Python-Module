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

    def grow(self, height):
        new_height = height + 1
        self.set_height(new_height)
        print(f"{self.name} grew 1 cm")

    def __str__(self):
        return f"{self.name}: {self.get_height}"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, is_blooming):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming


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


class Garden:
    def __init__(self, name, plants, plants_added, total_growtch):
        self.name = name
        self.plants = plants
        self.plants_added = 0
        self.total_growth = 0
        
    def add_plant(self, plants):
        if isinstance(self, Plant):
			