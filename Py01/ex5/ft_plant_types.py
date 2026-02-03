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
            print("Security: Negative height rejected")

class Flower(Plant):
    def	__init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        
    def bloom(self):
        print(f"{self.name} is blooming beautifully")

class Tree(Plant):
    def __init__(self, name, height, age,trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        print(f"{self.name} provide 78 square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age,harvest_season,nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        
rose = Flower("Rose",29,7,"red")
sunflower = Flower("Sunflower",42,18,"yellow")
flowers = [rose,sunflower]

oak = Tree("Oak",500,1825,50)
birch = Tree("Birch",450,1772,45)
trees = [oak,birch]

tomato = Vegetable("Tomato",80,45,"summer","Vitamine C")
pieckel = Vegetable("Pickel",75,15,"autum","Vitamine D")
vegetables = [tomato,pieckel]

for flower in flowers:
    print(f"{flower.name} (Flower): {flower.get_height()}cm, {flower.get_age()} days, {flower.color} color")
    flower.bloom()
    
for tree in trees:
    print(f"{tree.name} (Tree): {tree.get_height()}cm, {tree.get_age()} days, {tree.trunk_diameter} color")
    tree.produce_shade()
    
for vegetable in vegetables:
    print(f"{vegetable.name} (Vegetable): {vegetable.get_height()}cm, {vegetable.get_age()} days, {vegetable.harvest_season} harvest")
    print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")