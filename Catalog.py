import random
from Car import Car
import requests
import json



'''list of every car in catalog
is filled with cars right now for testing purposes, 
but final product will load in cars from JSON files'''

car_list = [Car('ford','mustang','2014','red',47859,20000.00,'manual',20),
            Car('chevrolet','silverado','2018','white',94877,28000.50,'automatic',14),
            Car('subaru','brz','2020','blue',50487,19450.00,'manual',3),
            Car('chevrolet','blazer','1991','dark green',20145,10000.00,'automatic',7),
            Car('dodge','challenegr','2010','black',111023,15000.00,'automatic',10)]

#dictionary that keeps track of the quantities of every make, every model, and every year
attribute_quantities:dict = {}

#placing data in attribute_quanitities to see if it works
for car in car_list:
    #counts total amount of specific year
    if not car.getMake() in attribute_quantities:
        attribute_quantities[car.getMake()]=1
    else:
        attribute_quantities[car.getMake()]+=1
    #counts total amount of specific model
    if not car.getModel() in attribute_quantities:
        attribute_quantities[car.getModel()]=1
    else:
        attribute_quantities[car.getModel()]+=1
    #counts total amount of specific year
    if not car.getYear() in attribute_quantities:
        attribute_quantities[car.getYear()]=1
    else:
        attribute_quantities[car.getYear()]+=1
    

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
        case 1:
            target = input("Please enter your desired Make: ").lower()
            for car in car_list:
                if car.getMake()==target:
                    found=True
                    print(car.toString()+'\n')
            if not found:
                print(f"No {target}s were found")
        case 2:
            target = input("Please enter your desired Model: ").lower()
            for car in car_list:
                if car.getModel()==target:
                    found=True
                    print(car.toString()+'\n')
            if not found:
                print(f"No {target}s were found")
        case 3:
            target = input("Please enter your desired year: ")
            for car in car_list:
                if car.getYear()==target:
                    found=True
                    print(car.toString()+'\n')
            if not found:
                print(f"No cars from {target} were found")





    
#test if sortByID works:
for i in car_list:
    print(i.getID())
car_list = sortByID(car_list)
print('\n')
for i in car_list:
    print(i.getID())

#test if findID works
#in the final product, SortBYID will be called before 
#findID is executed
print(findID(car_list,0,len(car_list)-1,10))
print(findID(car_list,0,len(car_list)-1,1))

print(attribute_quantities)

#testing the findSpecs function, UI will mkae process easier
findSpecs(1)
findSpecs(2)
findSpecs(3)
















#GET request to car API
'''api_url = 'https://api.api-ninjas.com/v1/cars?make={}&model={}&year={}'.format("ford","mustang","2014")
response = requests.get(api_url, headers={'X-Api-Key': 'F+ibc8OExQ83IKX/e3JJmQ==xsvvtTv25O4EXop3'})
data = response.json()
print(data!=[])'''

