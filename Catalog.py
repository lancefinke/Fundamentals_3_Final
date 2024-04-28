import random
from Car import Car
import json

class Catalog:

    def __init__(self):

        #list of every car in catalog
        self.car_list=[]
        #dictionary that keeps track of the quantities of every make, every model, and every year
        self.attribute_quantities:dict= {}

    def setCarList(self,list):
        self.car_list=list
    
    def getCarList(self):
        return self.car_list


    def  updateDict(self, car:Car): #called when adding a car
        if not car.getMake() in self.attribute_quantities:
            self.attribute_quantities[car.getMake()]=1
        else:
            self.attribute_quantities[car.getMake()]+=1
    
        if not car.getModel() in self.attribute_quantities:
            self.attribute_quantities[car.getModel()]=1
        else:
            self.attribute_quantities[car.getModel()]+=1
   
        if not car.getYear() in self.attribute_quantities:
            self.attribute_quantities[car.getYear()]=1
        else:
            self.attribute_quantities[car.getYear()]+=1
    


    #loads Json data and creates car_list
    def loadData(self):
        with open("Car_Storage.json","r") as file:
            data=json.load(file)
            for object in data:
                tempCar = Car(object["make"],object["model"],object["year"],object["color"],
                            object["mileage"],object["price"],object["transmission"],object["ID"],)
                if object["verified"]==True:
                    tempCar.verify()
                self.updateDict(tempCar)
                self.car_list.append(tempCar)



    def sortByID(self,list): #quicksort algorithm
        if len(list)<2:
            return list
        else:
            #chooses random index in car_list and gets that car's ID
            pivotCar = list[random.randint(0,len(list)-1)]
            pivotID=pivotCar.getID()
            #less array contains all cras with IDs less than pivotID
            less = [i for i in list if i.getID() <=pivotID]
            #more array contains all elements 
            more  = [i for i in list if i.getID() > pivotID]
            return self.sortByID(less) + self.sortByID(more)
    

    def findID(self,list,low,high,ID): #binary search algorithm
        if high >= low:

            #finds midpoint
            mid = (high+low) // 2

            #returns car information of ID matches
            if list[mid].getID() == ID:
                return list[mid].toString()
        
            elif list[mid].getID() > ID:
                return self.findID(list,low,mid-1,ID)
        
            else:
                return self.findID(list,mid+1,high,ID)
        
        else:
            return f'Could not find a car with ID number of {ID}'
    
#returns all cars of a specific make, model, or year
#user will be promted to enter in a number based on what they want to find
    def findSpecs(self,action:int): #linear search algorithm
            match action:
                case 1:
                    make = input("Enter a specific make: ").lower()
                    if not make in self.attribute_quantities:
                        print(f"No {make}s were found\n")
                    else:
                        print(f"Amount of {make}s found: {self.attribute_quantities[make]}\n")
                        for car in self.car_list:
                            if(car.getMake()==make):
                                print(car.toString())
                case 2:
                    model = input("Enter a specific model: ").lower()
                    if not make in self.attribute_quantities:
                        print(f"No {model}s were found\n")
                    else:
                        print(f"Amount of {model}s found: {self.attribute_quantities[model]}\n")
                        for car in self.car_list:
                            if(car.getModel()==model):
                                print(car.toString())
                case 3:
                    year = input("Enter a specific year: ")
                    if not year in self.attribute_quantities:
                        print(f"No Cars from {year} were found\n")
                    else:
                        print(f"Amount of cars from {year} found: {self.attribute_quantities[make]}\n")
                        for car in self.car_list:
                            if(car.getYear()==year):
                                print(car.toString())
                

    #saves car list data to JSON file can be called manually but is also called automatically when program terminates
    def saveToJSON(self):
        newData = []
        for car in self.car_list:
            carObj = {
            "make":car.getMake(),
            "model":car.getModel(),
            "year":car.getYear(),
            "color":car.getColor(),
            "mileage":car.getMiles(),
            "price":car.getPrice(),
            "transmission":car.getTrans(),
            "ID":car.getID(),
            "verified":car.getVerification()
            }
            newData.append(carObj)
        with open("Car_Storage.json", 'w') as file:
            json.dump(newData,file,indent=4)

    def displayCars(self):
        for car in self.car_list:
            if car.getVerification()==True:
                print(f"\nVERIFIED\n{car.toString()}")
            else:
                print(f"\n!!!NOT VERIFIED!!!\n{car.toString()}")

            
            
        

        



    












