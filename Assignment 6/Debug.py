class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:

    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Eddie" , 7)
    print(newDog.name, newDog.age)
    
    #and what about a new employee
    newEmployee = Employee("Tommy", 18, "HR")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make

    newCake = Cake("Chocolate", "Fondant")

    print(newCake.flavor, newCake.frosting)
    
    
    
    #and now create another cake and print it out

    secondCake = Cake("Vanila", "Fudge")

    print(secondCake.flavor, secondCake.frosting)
    
    
    
    #create a cat!
    cat1 = Cat("Mittens", "2", "long")
    #create another cat!
    cat2 = Cat("Mouse", "8", "short")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.name, cat1.age, cat1.breedGuess())
    
    #create a car!

    newCar = Car("Tesla", 2023, "Red")
    
    #Now print out the function you made for car :)

    print(newCar.model, newCar.year, newCar.color)

main()
