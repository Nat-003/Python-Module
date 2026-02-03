class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self.__heigh = height
        self.__age = age

    def get_height(self):
        return self.__heigh
    
    def get_age(self):
        return self.__age
    
    def set_height(self):
        self.__height = height
        
rose = Plant("Rose","40cm","39 days")
        