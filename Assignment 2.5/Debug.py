
def main():

    #that's not right... how can we make sure it also includes equals 5?
    temp = 5
    if temp >= 5:
        print("temp is greater than or equal to 5")
        
    
    #enter your name here
    name = "Tommy"
    #in this if/elif/else, add 4 mispellings of your name for if/elif comparisons, and then have your last elif be elif name = "your properly spelled name" '''
    if name == "Tomy":
        print("That's not right!")
    elif name == "Ttomy":
        print("That's not right!")
    elif name == "Tommmy":
        print("That's not right!")
    elif name == "Tomm":
        print("That's not right!")
    elif name == "Tommy":
        print("That's right")
    else:
        print("I don't know who that is")
    #etc etc, the else can be whatever you want
    
    
    #we're gonna check if a user input number is even
    #pick any number
    even = int(input("Enter a number to find out if its even or odd: "))
    even = int(even)
    #what do we replace the question marks with?
    if even % 2 == 0:
        #what would be appropriate in these print statements?
        print("The number is even")
    else:
        print("The number is odd")
  
  
    #i'm trying to do math with the numbers 2 and 4, but it's getting 3 and 5... why?
    numbers = [1,2,3,4,5]
    print(numbers[1])
    print(numbers[3])
    print(numbers[3] / numbers[1])
    print(numbers[3] * numbers[0])
    
    #again, why is it getting 7 and 20, I wanted 3 and 29!
    numbers2 = [465,3,30,7,29,20,82,13,5]
    print(numbers2[1])
    print(numbers2[4])
    
    #My name was not in here so I added it!
    #Here's a fun one: This is a list of everyone's name. Find where yours is and print the index of your name
    students = ["Achorn, Cameron", "Blanche, Tommy", "Brown, Evan", "Catalano, Alexander", "Cianfoni, Alexander", "Delorey, Tyler","Edmonds, Jonah","Elliott, Dustin","Faix, Joseph","Fleischman, Connor","Fuerte, Caroline","Gidos, Hannah","Lavitt, Samuel","Lichstein, Harris","Longo, Nicholas","Martinez, David","Muggeri, Mattia","Munger, Ryan","Nealon, Ryan","Paulus, Natalie","Penn, Riley","Potenza, Amanda","Prochet, Carlisl","Putkaradze, Saba","Quayson, Eugene","Rietti, Cristina","Seeley, Shane","Sweeney, Quinn","Tata, Mathew","Taylor, Julia","Tuozzo, Michael"]
    print(students[1])

main()
    
    

    
