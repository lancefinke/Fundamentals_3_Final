class Car:


    def __init__(self,make,model,year,color,mileage,transmission,ID):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.mileage=mileage
        self.transmission=transmission
        self.ID=ID

    #All of the access methods

    def getMake(self):return self.make
    def getModel(self):return self.model
    def getYear(self):return self.year
    def getColor(self):return self.color
    def getMiles(self):return self.mileage
    def getTrans(self):return self.transmission
    def getID(self):return self.ID

    #All of the modifier methods

    def setMake(self,newMake):self.make=newMake
    def setModel(self,newModel):self.model=newModel
    def setYear(self,newYear):self.year=newYear
    def setColor(self,newColor):self.color=newColor
    def setMiles(self,newMileage):self.mileage=newMileage
    def setTrans(self,newTransmission):self.transmission=newTransmission
    def setID(self,newID):self.ID=newID
    



