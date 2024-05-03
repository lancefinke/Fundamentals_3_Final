from time import sleep
from numpy import double
import requests
from Car import Car
from Catalog import Catalog as carCatolog
#used to validate date enteres
import re
import os

Main_Catalog = carCatolog()
Main_Catalog.loadData()


#keeps track of every used ID.
used_IDs = []
for car in Main_Catalog.getCarList():
    used_IDs.append(car.getID())

print(used_IDs)


#array that validates date
regex =[r"^[1][9]+$",r"^[2][0]+$",r"^[0,1][0-9]+$",r"^[2][0-4]+$"]



'''verifies that the make, model and year enetred
    are indeed from a real car.'''
def verifyCar(car:Car):
    make = car.getMake().lower()
    model = car.getModel().lower()
    year = car.getYear()

    api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format(make,model,year)
    response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
    data = response.json()
    if(data!=[]):
        car.verify()

print("\nWelcome to the Car Catalog!")

while True:
    sleep(1)
    print( "\nPlease enter in a command or type 'Help' for Help\n")
    print("\n1) List All Cars\n2) Add Car\n3) Remove Car\n4) Save Data\n5) Sort Cars\n6) Find Car\n7) Find cars with specific make, model or year\n8) Exit\n")
    choice = input("Enter in a command: ").lower()#makes help command case insensitive
    match choice:
        case 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            with open("User Manual.txt","r") as file:
                text  = file.read()
                print(text)
            sleep(10)
        case '1':
            Main_Catalog.displayCars()
        case '2': 
            make = input("\nWhat is the Car's make: ").lower()
            model = input("\nWhat is the Cars model: ").lower()
            year = ""
            while True:
                year = input("\nwhat year was the car made: ")
                if len(year)==4:
                    if re. match(regex[0], year[:2]):
                        if re. match(r"^\d\d+$",year[2:]):
                            break
                        else:
                           print("\nPlease enter in a valid year")
                    elif re. match(regex[1],year[0:2]):
                        if  re. match(regex[2],year[2:]) or re. match(regex[3],year[2:]):
                            break
                        else:
                           print("\nPlease enter in a valid year") 
                    else:
                        print("\nPlease enter in a valid year") 
                else:
                    print("\nPlease enter in a valid year")
            color = input("\nWhat color is the car: ")
            mileage = 0
            while True:
                try:
                    mileage = int(input("\nHow many miles does the car have: "))
                    break
                except:
                    print("\nPlease Enter in a number.\n")
            price = 0.0
            while True:
                try:
                    price = float(input("\nHow much is the car worth: "))
                    break
                except:
                    print("\nPlease Enter in a valid price.\n")
            trans = ""
            while True:
                print("What type of transmission does this car have?")
                print("\n1) Automatic\n2) Manual\n3) Exit")
                option = input("\nEnter option: ")
                match option:
                    case '1':
                        trans = "automatic"
                        break
                    case '2':
                        trans = "manual"
                        break
                    case '3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    case _:
                        print("\nPlease enter either '1' or '2'\n")
            ID=0
            while True:
                used=False
                try:
                    ID = int(input("\nPlease enter a unique ID number: "))
                    for i in used_IDs:
                        if i==ID:
                            used=True
                    if not used:
                        used_IDs.append(ID)
                        break
                    else:
                        print(f"\nID Number {ID} is already being used.")
                except:
                    print("\nPlease enter in a number.\n")
            tempCar = Car(make,model,year,color,mileage,price,trans,ID)
            verifyCar(tempCar)
            Main_Catalog.getCarList().append(tempCar)
            Main_Catalog.updateDict(tempCar)
        case '3':
            try:
                index = int(input("\nEnter the index of the Car you would like to remove: "))-1
                if(index<len(Main_Catalog.getCarList()) and Main_Catalog.getCarList()[index].getID() in used_IDs):
                    ID = Main_Catalog.getCarList()[index].getID()
                    for i in range(len(used_IDs)-1):
                        if used_IDs[i]==ID:
                            used_IDs.pop(i)
                    Main_Catalog.getCarList().pop(index)
                    print(f"Car at index {index+1} was removed.")
                else:
                    print("Index entered was out of range.")
            except:
               print("\nInvalid Input")
        case '4':
            Main_Catalog.saveToJSON()
            print("\nData saved.")
        case '5':
            sortedList = Main_Catalog.sortByID(Main_Catalog.getCarList())
            Main_Catalog.setCarList(sortedList)
            print("\nCars are now sorted by ID")
        case '6':
            try:
                ID = int(input("\nPlease enter the ID of the car you want to find: "))
                sortedList = Main_Catalog.sortByID(Main_Catalog.getCarList())
                Main_Catalog.setCarList(sortedList)
                print(Main_Catalog.findID(Main_Catalog.getCarList(),0,len(Main_Catalog.getCarList())-1,ID))
            except:
                print("\nInvalid Input.")
        case '7':
            print("\nWhat would you like to find?:\n1) A certain make\n2) A certain model\n3) A certain year")
            choice = input("\nYour Choice: ")
            match choice:
                case '1':
                    Main_Catalog.findSpecs(1)
                case '2': 
                    Main_Catalog.findSpecs(2)
                case '3':
                    Main_Catalog.findSpecs(3)
                case _:
                    print("\nInvalid Option Selected.")
        case '8':
            Main_Catalog.saveToJSON()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saving and Exiting...")
            sleep(1.5)
            break
        case _:
            print("Command not recognized by program.")

                    
                
            
