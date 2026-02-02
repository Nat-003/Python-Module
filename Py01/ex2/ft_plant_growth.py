class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def age_plant(self):
        self.age += 1

    def grow(self):
        self.height += 1 

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

rose = Plant("Rose",25,30)
sunflower = Plant("Sunflower",80,45)
cactus = Plant("Cactus",15,120)
plants = [rose,sunflower,cactus]


for i in range(1,8):
    for plant in plants:
        if i == 1:
            print(f"Day {i}")
            print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
            plant.grow()
        elif i == 7:
            print(f"Day {i}")
            print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
        else:
            plant.grow()
