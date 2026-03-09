class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, height):
        if height >= 0:
            self.__height = height
            print(f"Height updated:{height} cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")

    def set_age(self, age):
        if age >= 0:
            print(f"Age updated:{age} days [OK]")
            self.__age = age
        else:
            print("Security: Negative height rejected")


rose = Plant("Rose", -40, 39)


print(rose.get_height())
print(rose.get_age())

