import random
from time import sleep
from Car import Car
import requests
import json

#list of every car in catalog
car_list=[]
#dictionary that keeps track of the quantities of every make, every model, and every year
attribute_quantities:dict = {}




def  updateDict(car:Car): #called when adding a car
    if not car.getMake() in attribute_quantities:
        attribute_quantities[car.getMake()]=1
    else:
        attribute_quantities[car.getMake()]+=1
    
    if not car.getModel() in attribute_quantities:
        attribute_quantities[car.getModel()]=1
    else:
        attribute_quantities[car.getModel()]+=1
   
    if not car.getYear() in attribute_quantities:
        attribute_quantities[car.getYear()]=1
    else:
        attribute_quantities[car.getYear()]+=1

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
    


#loads Json data and creates car_list
with open("Car_Storage.json","r") as file:
    data=json.load(file)
    for object in data["Garage"]:
        tempCar = Car(object["make"],object["model"],object["year"],object["color"],
                            object["mileage"],object["price"],object["transmission"],object["ID"],)
        if object["verified"]==True:
            tempCar.verify()
        updateDict(tempCar)
        car_list.append(tempCar)



def sortByID(list): #quicksort algorithm
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
        return sortByID(less) + sortByID(more)
    

def findID(list,low,high,ID): #binary search algorithm
    if high >= low:

        #finds midpoint
        mid = (high+low) // 2

        #returns car information of ID matches
        if list[mid].getID() == ID:
            return list[mid].toString()
        
        elif list[mid].getID() > ID:
            return findID(list,low,mid-1,ID)
        
        else:
            return findID(list,mid+1,high,ID)
        
    else:
        return f'Could not find a car with ID number of {ID}'
    
#returns all cars of a specific make, model, or year
#user will be promted to enter in a number based on what they want to find
def findSpecs(action:int): #linear search algorithm
    found=False
    match action:
        case 1: #finds all desired models
            target = input("Please enter your desired Make: ").lower()
            for car in car_list:
                if car.getMake()==target:
                    found=True
                    print(car.toString()+'\n')
            if not found:
                print(f"No {target}s were found")
        case 2: #finds all desired makes
            target = input("Please enter your desired Model: ").lower()
            for car in car_list:
                if car.getModel()==target:
                    found=True
                    print(car.toString()+'\n')
            if not found:
                print(f"No {target}s were found")
        case 3: #finds all desired years
            target = input("Please enter your desired year: ")
            for car in car_list:
                if car.getYear()==target:
                    found=True
                    print(car.toString()+'\n')
            if not found:
                print(f"No cars from {target} were found")


def updateJSON(car:Car):
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



while True:
    print("Welcome to the Car Catalog. Please enter in one of the commands below, or type H for help.\n");
    print("1) Add Car\n2) Remove Car\n3) List Catalog\n4) Find Car\n5)Find Cars with specific make model or year\n6) Sort Cars by ID\n7) Exit")
    choice = (int)(input())
    match choice:
        case
        case 7:
            print("Exiting Catalog...")
            sleep(1.5)
            break







