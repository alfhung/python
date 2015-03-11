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
        return self.__speed

    def brake(self):
        self.__speed = self.__speed - 5
        return self.__speed

    # method returns current speed
    def get_speed(self):
        return self.__speed

# program create car object
# calls accelerate method 5 times
# return current speed after each call to accelerate
# then calls brake method 5 times
# return current speed after each call to brake

def car(year_model,make):
    # create object from car
    car_obj = Car(year_model,make)

    # call function to display car model and made
    model = car_model(car_obj)

    # call functions to display speed after accelerating
    # and braking 5 times
    speed_accelerate = accelerating(car_obj)
    speed_brake = braking(car_obj)
    
# display the model of the car
def car_model(car_obj):
    print('The model of your car is %d' % (car_obj.get_model()))
    print('Your car is made of ' + car_obj.get_make())

# call accelerate method 5 times, then display speed
def accelerating(car_obj):
    for num in range(5):
        speed = car_obj.accelerate()

    print('The current speed is ',speed)

# call brake method 5 times, then display speed
def braking(car_obj):
    for value in range(5):
        speed = car_obj.brake()

    print('The current speed is ',speed)
