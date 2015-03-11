import sqlite3
from tkinter import *
import citiesDBClass
import cityClass

# GUI Interface for Cities in the world info

class CityGUI:
    # construct window that contains
    # picture location, entry for city, button labels
    # show results on bottom on window
    def __init__(self):
        self.cityProfile = citiesDBClass.CitiesDB()
        self.root = Tk()
        self.root.title('City Database')

        # create components user see when start program
        image = self.pictureFrame()
        cityButton = self.buttonFrame()
        cityEntry = self.cityFrame()

        self.root.mainloop()
        
    # create frame to hold picture
    def pictureFrame(self):
        picFrame = Frame(self.root)
        picFrame.grid(row=0,column=0)

        # obtain image to place on window
        # place name of image in file
        self.image = PhotoImage(file = 'SeeTheWorldTravel3.gif')
        # create label for picture
        image = Label(picFrame, image = self.image)
        image.pack()

        return picFrame

    # create frame for buttons
    def buttonFrame(self):
        cityButtonFrame = Frame(self.root)
        cityButtonFrame.grid(row=1,column=0)

        self.startButton =Button(cityButtonFrame, text='Start',\
                                 width = 30,\
                                 command = self.activate)
        self.startButton.grid(row=0)

        return cityButtonFrame

    # activate show profile button to start
    def activate(self):
        self.showInfo.config(state='normal')
        self.startButton.config(activeforeground='blue',state='disabled')
        
    # create frame with instruction, entry and button for city profile
    def cityFrame(self):
        cityEntryFrame = Frame(self.root)
        cityEntryFrame.grid(row = 0, column = 1)

        instructions = 'Enter Name of City:'
        instructLabel = Label(cityEntryFrame, text = instructions)
        instructLabel.grid(row = 0)

        self.cityEntry = Entry(cityEntryFrame, width = 20)
        self.cityEntry.grid(row = 1)

        self.showInfo = Button(cityEntryFrame,text='Show City Profile',\
                               command = self.results,\
                               state = 'disabled'
                               )
        self.showInfo.grid(row=2)

        return cityEntryFrame

    # mutator get city, validate if city in DB
    def validCity(self,cityName):
        city = self.cityProfile.queryDB(cityName)
        if city == None:
            messagebox.showerror('Error!!\n',\
                                 'City Entered is not in Database,\n'
                                 'Please Enter a New City')
        else:
            return city

    # callback method for show city profile button
    # create window to show results
    def results(self):
        cityName=self.cityEntry.get()
        # call function to validate input
        cityInfo = self.validCity(cityName)
        if cityInfo != None:
            # get name of city from list
            city = cityInfo[0]

            # create city object        
            self.cityObject = cityClass.City(cityInfo[0],cityInfo[1],\
                                         cityInfo[2],cityInfo[3],\
                                         cityInfo[4])

            # create new window to show results
            infoWindow = Toplevel()
            infoWindow.title('Information for City')
        
            # create city picture object
            self.cityPicture = cityClass.Picture()
        
            infoPicture = Frame(infoWindow)
            infoPicture.grid(row = 0, column = 0)

            # place picture in result window
            picture = self.cityPicture.cityPic(city)
            self.cityImage = PhotoImage(file = picture)
            picLabel = Label(infoPicture,image=self.cityImage)
            picLabel.pack()

            # write city data into result window
            cityData = self.cityProfile.viewCityInfo(city)
            infoText = Text(infoWindow, width = 50)
            infoText.grid(row = 0, column = 1)
            infoString = ''
            for line in cityData:
                infoString = ''+str(line)+'\n'                       
                infoText.insert(END, infoString)
            
            infoText.config(state = 'disabled')

# create cityGUI object
CityGUI()
