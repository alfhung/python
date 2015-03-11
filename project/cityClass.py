# create class definition for a city

class City:
    # define constructor
    def __init__(self,city,country,population,\
                 language,places):
        self.__city = city
        self.__country = country
        self.__population = population
        self.__language = language
        self.__places = places

    # define accesors
    def getCity(self):
        return self.__city

    def getCountry(self):
        return self.__country

    def getPopulation(self):
        return self.__population

    def getLangugae(self):
        return self.__language

    def getPlaces(self):
        return self.__places

class Picture:
    # create list of picture names
    def __init__(self):
        self.__cityPicNameList = []
        picFile = 'citiespicturenames.txt'
        getPicFile = open(picFile,'r')
        for pic in getPicFile:
            picName = pic.strip()
            self.__cityPicNameList.append(picName)

    # method search city picture in list
    def cityPic(self,cityName):
        newCityName = cityName.lower()
        check = True
        index = 0
        while check == True:
            name = self.__cityPicNameList[index]
            picName = name[:len(name)-4]
            if picName == newCityName:
                check = False
                return name
            else:
                index = index + 1
