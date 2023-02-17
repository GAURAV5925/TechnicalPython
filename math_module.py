#My method


def search_letter(name):
    j=0
    for i in name:
        if i=='a':
            print("The letter is present at",j,"of value",name)
            break                ##If we will remove the break keyword we can get the next letter also which are present in the string
        j = j+1


def palindrome(name):
    for i in range(0, int(len(name)/2)):
        if name != name[len(name)-1-i]:
            print("Palindrome")
            break
        else:
            print("Not a Palindrome")


def bigthree():
    a = int(input("Enter the value of A: "))
    b= int(input("Enter the value of B: "))
    c= int(input("Enter the value of C: "))

    if a>b and a>c:
        print("A is the largest")
    elif b>c and b>a:
        print("B is the largest")
    elif a==b and a==c:
        print("A, B and C are equal")
    else:
        print("C is the largest")


def arith(value1,value2,value3):
    add = value1 + value2 + value3
    product = value1 * value2 * value3
    subtraction = value1 - value2 - value3

    return add,product,subtraction

