class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age

rose = Plant('Rose',"25cm",30)
sunflower = Plant("Sunflower","80cm",45)
cactus = Plant("Cactus","15cm",120)
plants = [rose,sunflower,cactus]
for plant in plants:
    print(f"{plant.name}: {plant.height}, {plant.age} days old")