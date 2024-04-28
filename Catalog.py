import random
from time import sleep
from Car import Car
import requests
import json

class Catalog:

    def __init__(self):

        #list of every car in catalog
        self.car_list=[]
        #dictionary that keeps track of the quantities of every make, every model, and every year
        self.attribute_quantities:dict= {}




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

    '''verifies that the make, model and year enetred
    are indeed from a real car.'''
    def verifyCar(self,car:Car):
        make = car.getMake().lower()
        model = car.getModel().lower()
        year = car.getYear()

        api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format(make,model,year)
        response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
        data = response.json()
        if(data!=[]):
            car.verify()
    


    #loads Json data and creates car_list
    def loadData(self):
        with open("Car_Storage.json","r") as file:
            data=json.load(file)
            for object in data["Garage"]:
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
        while True:
            match action:
                case 1:
                    make = input("Enter a specific make: ").lower()
                    if not make in self.attribute_quantities:
                        print(f"No {make}s were found\n")
                    else:
                        print(f"{self.attribute_quantities[make]} {make}s were found.\n")
                        for car in self.car_list:
                            if(car.getMake()==make):
                                print(car.toString())
                        break
                


    def updateJSON(self, car:Car):
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
        with open("Car_Storage.json", 'r+') as file:
            data = json.load(file)
            data["Garage"].append(carObj)
            file.seek(0)
            json.dump(data,file,indent=4)





c = Catalog()
c.car_list.append(Car("ford","mustang","2014","red",100000,20000.00,"manual",50))
c.updateDict(Car("ford","mustang","2014","red",100000,20000.00,"manual",50))

c.findSpecs(1)







