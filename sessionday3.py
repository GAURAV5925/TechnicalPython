##for do while break pass continue- todays topic

## ASCII Code For the Letters
## 65-91 --> A-Z 
## 97-122 --> a-z 
## 48-57 -->  No's(0-9)

##check if passed in all the paper

'''
a= int(input("Enter the a value"))
b = int(input("ENter the b value"))
c= int(input("ENter the c value"))
d= int(input('Enter the d value'))


## To Check if the person passed all the paper


if (a>=40) and (b>=40) and (c>=40) and (d>=40):
    print("Passed")
else:
    print("Failed")'''


## WAP to check entered no's is positive or not


'''a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number "))

if a>=0:
    print("Given Number is positive")
elif a==0:
    print("Given number is Negative")
else:
    print("Given number is Negative")

'''


##Check if letter is Vowel or Consonent

'''

letter=input("Please enter the letter")

letter.lower()

if (letter=="a" or letter=="A") or (letter=="e" or letter=="E") or (letter=="i" or letter=="I") or (letter=="o" or letter=="O") or (letter=="u" or letter=="U"):
    print("Vowel")
else:
    print("Consonent")

vowel_list = ('a','e','i','o','u','A','E','I','O','U')

vowel_set = ['a','e','i','o','u','A','E','I','O','U']

if letter in vowel_list:
    print("It's vowel")
else:
    print("It's consonent")

if letter in vowel_set:
    print("It's vowel")
else:
    print("It's consonent")
'''


## TO CHECK WEATHER THE ENTERED VALUE IS CHAR IN UPPERCASE OR LOWERCASE AND  NUMBER 
#this code will convert the Char, Digit and No's into ASCII value which will 



'''if ch>=65 and ch<=91:
    print("Your entered character is in uppercase")
elif ch>=97 and ch <= 122:
    print("Your entered character is in lower case")
elif ch>=48 and ch<=57:
    print("Your entered character is digit")
else:
    print("your entered char is in special symbols")'''


## To calculate the sum of first 10 Natural No's

'''no = 10
sum=0

while no >0:
    sum=sum+no
    no=no-1

print("The sum is", sum)'''


##FIBONACCI SERIES(My Code)

Number = 8

# Initializing First and Second Values
i = 0
First_Value = 0
Second_Value = 1
           
# Find & Displaying
while(i < Number):
    if(i <= 1):
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
    i = i + 1



    




