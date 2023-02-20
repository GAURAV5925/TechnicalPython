# Q1. Area of triangle

'''
class Homework:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        self.areaoftriangle = (1*(self.base*self.height) )/2
        print("The area of the triangle is: ", self.areaoftriangle)

base = int(input("Enter the value of the base: "))
height = int(input("Enter the value of the Height of: "))

obj = Homework(base,height)
obj.area()
'''

# Q2. Swapping of two variable

'''class Swaping:
    def __init__(self):
        self.value1=120
        self.value2=89

    def swapping(self):
        self.value1 = self.value1 + self.value2
        self.value2 = self.value1  - self.value2
        self.value1 = self.value1 - self.value2
        print(self.value1,self.value2)

obj = Swaping()
obj.swapping()
'''

# Q3. Leap Year checking

'''
class LeapYear:
    def __init__(self):
        self.year = int(input("Enter the year: "))
    
    def checkleap(self):
        if (self.year%400==0) and (self.year%100==0):   #Here some case can be exception for the leap years like 1900 was not a leap year so we check weather it is divisible by 100 and 400 both 
            print("Leap Year")
        elif (self.year%4==0) and (self.year%100!=0):
            print("Leap Year")
        else:
            print("Not a leap year")

obj = LeapYear()
obj.checkleap()
'''

# Q4. Simple Calculator

class Calculator:
    def __init__(self):
        self.option = int(input("Please Enter the operation that you want to perform \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n "))
        if (self.option != 1) and (self.option !=2) and (self.option !=3) and (self.option !=4): 
            print("Not a valid option")
        else:
            self.value1=float(input("Please Enter your 1st number"))
            self.value2=float(input("Please Enter your 2nd Number"))
        
        
        

    def operation(self):
        if self.option==1:
            print("Addition of the two value is : ", self.value1+self.value2)
        elif self.option==2:
            print("Subtraction of the two value is : ", self.value1-self.value2)
        elif self.option == 3:
            print("Multiplication of the two value is : ", self.value1*self.value2)
        elif self.option == 4:
            print("Division of the two values is : ", self.value1 / self.value2)
        else:
            print("Please enter a valid option")


obj = Calculator()
obj.operation()



# Q5. Celcius to Faraenhite

'''
class Faranheit:
    def __init__(self):
        while True:
            self.option = int(input("Enter your choice in which manner you want to convert\n 1. Celcius to Faranheit\n 2. Faranheit to Celcius\n "))
            if self.option == 1:
                self.temp = float(input("Enter the Temperature in the Celcius"))
                break
            elif self.option == 2:
                self.temp = float(input("Enter the Temperature in the Faranheit"))
                break
                
            else:
                print("Please enter a valid option")
                


    def tempcalc(self):
        if self.option==1:
            self.faran=((self.temp*9)/5) + 32
            print("Temperature in Faranheit will be: ", self.faran)
        elif self.option==2:
            self.celc = ((self.temp-32)*5)/9
            print("Temperature in the celcius will be : ", self.celc)
        else:
            print("Please enter a valid option")

obj = Faranheit()
obj.tempcalc()'''