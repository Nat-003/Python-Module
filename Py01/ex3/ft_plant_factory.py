class Plant:
    count = 0
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1

rose = Plant("Rose",25,"30 days")
oak = Plant("Oak",200,"265 days")
cactus = Plant("Cactus",5,"90 days")
sunflower = Plant("Sunflower", 80,"45 days")
fern = Plant("Fern", 15,"120 days")

plants = [rose,oak,cactus,sunflower,fern]

for plant in plants:
	print(f"Created: {plant.name} ({plant.height}, {plant.age})")
print(f"Total plants created: {Plant.count}")

rose.height = 32 
print(f"la hauteur de la rose est de {rose.height}")