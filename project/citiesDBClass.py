import sqlite3

# define class representing database
# database contains info about cities

class CitiesDB:
    # constructor
    def __init__(self):
        self.__connection = sqlite3.connect('Places')
        self.__cursor = self.__connection.cursor()

    # create table named cities
    # each row in table contains info about a city
    # categories for each city are:
    # name, population, language, interesting places, interesting facts
    def createCitiesTable(self):
        self.__cursor.execute('drop table if exists cities')
        self.__cursor.execute('''create table cities(
                                name text,
                                country text,
                                population integer,
                                language text,
                                places text)'''
                              )

        cityNames = 'cities.txt'
        cityFile = open(cityNames, 'r')
        for line in cityFile:
            info = line.strip()
            data = info.split(';')
            cityName = data[0]
            cityCountry = data[1]
            cityPopu = data[2]
            cityLanguage = data[3]
            cityPlaces = data[4]
            cityInfo = (cityName,cityCountry,cityPopu,cityLanguage,cityPlaces)
            self.__cursor.execute('''insert into cities(
                                    name, country, population, language, places)
                                    values (?,?,?,?,?)''',cityInfo
                                  )

        self.__connection.commit()
        print('City Table Created')

    # accesor display all info in table
    def viewCityTable(self):
        self.__cursor.execute('''select * from cities''')
        info = self.__cursor.fetchall()
        info_index = 0
        print('City Name          Country          Population         Language          Places')
        for line in info:
            print('%s          %s         %s          %s          %s' \
                  %(line[0],line[1],line[2],line[3],line[4]))        

    # mutator to view individual city info
    def viewCityInfo(self, cityName):
        self.__cursor.execute('select * from cities where name=?',\
                              (cityName,)
                              )
        city = self.__cursor.fetchone()
        city_index = 0
        self.cityInfo = []
        categories = ['City Name','Country','Population','Language','Places']
        for info in categories:
            cityData = info+':  '+str(city[city_index])
            self.cityInfo.append(cityData)
            city_index = city_index + 1
        return self.cityInfo
    
    # accesor to query database
    def queryDB(self, cityName):
        self.__cursor.execute('select * from cities where name=?',\
                              (cityName,)
                              )
        city = self.__cursor.fetchone()
        return city
    
    # mutator to close connection
    def closeCitiesDB(self):
        self.__connection.close()
        
CitiesDB()
