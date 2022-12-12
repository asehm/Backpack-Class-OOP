# Backpack Class Assignment

class Backpack():
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    def openBag(self):
        self.open = True
        print("Bag has been opened!")

    def closeBag(self):
        self.open = False
        print("Bag has been closed!")
    
    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print(self.items)
            print(f"{item} has been added to the bag!")
    
    def takeout(self, item):
        if self.open == True:
            if item in self.items:
                self.items.remove(item)
                print(self.items)
                print(f"{item} has been removed from the bag!")
            else:
                print(f"{item} was not removed as it wasn't in the bag!")


smallBlue = Backpack("Blue", "Small")
mediumRed = Backpack("Red", "Small")
largeGreen = Backpack("Green", "Large")
        
smallBlue.openBag()         #open
smallBlue.putin("lunch")    #put in your lunch
smallBlue.putin("jacket")   #put in your jacket
smallBlue.closeBag()        #close
smallBlue.openBag()         #open
smallBlue.takeout("jacket") #take out your jacket
smallBlue.closeBag()        # Close

