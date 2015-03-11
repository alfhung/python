# define class definition for a car
class Car:
    # define constructor
    def __init__(self,year_model,make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # define accesor methods
    def get_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    # define mutator methods
    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self,speed):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed
