#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random
class student:

    def __init__(self, name, studentId, year, major, gpa):
        self.name = name
        self.studentId = studentId
        self.year = year
        self.major = major
        self.gpa = gpa

    def eligibility(self):
        if self.gpa > 3.5:
            return "true"
        else:
            return "false"

    def wacky(self):

        generate = random.randint(0000, 9999)



        if self.studentId == generate:
            print("winner! " + self.name + " gets free lunch!")
        else:
            print("Loser!")


def main():

    one = student("Jackson", 4328, "s", "data science", 3.6)

    two = student("Tomas", 9238, "j", "comp sci", 3.8)

    three = student("Pat", 4630, "s", "business", 1.2)
    #create three students and check if they get free lunch and if they qualify for honors

    print(one.name, one.studentId, one.year, one.major, one.gpa, one.eligibility(), one.wacky())

    print(two.name, two.studentId, two.year, two.major, two.gpa, two.eligibility(), two.wacky())

    print(three.name, three.studentId, three.year, three.major, three.gpa, three.eligibility(), three.wacky())


main()
