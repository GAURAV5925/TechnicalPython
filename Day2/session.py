###List


myList = ["Gaurav","jha","random","sample","something"]

print(myList)
print(myList[0])
print(myList[2:5])
print(myList[1:6:2])

myList[2] = "Nothing"
print(myList)

myList.append("Amazing")            #Will append the element at the last of the list
print(myList)

myList.insert(3,"New Value")
print(myList)

mylist3=[44,22,77,0,9,88]
print(0 in mylist3)  ##checks if the element is present in the list it is type of MEMBERSHIP
print(100 in mylist3)

#2D List

mylist = [['gaurav','jha'],['85.56'],[440022,"yyy"]]
print("example of multidimensional list")
print(mylist[0][0])                                       #print(mylist[row][col])

list2 = [44,22,77,0,9,88]                                 
list2.sort()                              #this will sort the array in ascending order
print(list2)

#### Tupple

mytuple = ("Gaurav","Jha","Random","Amazing","Something")
print(mytuple)
print(type(mytuple))
# mytuple[2] = 'sunil' Tuple is immutable meaning any operation on it is not possible
print(mytuple)

### Dictionary : It is in key:value pair which allow us to uniquely identify any element

mydict = {
    101:"Gaurav",
    "professional": "developer",
    "emid" : 1001
}

mydict.pop(101)
print(mydict)


### Set : in the set operator we can only add the unique elements
### Arrangmenet of the set are the unordered or random manner meanining we cant predict the way it will be arranged

myset = {10,20,30,40}
yourset = {"Gaurav","Jha"}

print(myset)

myset.add(60)
print(myset)

myset.remove(30)
print(myset)

myset.discard(40)
print(myset)



myset = {10,20,30,40}
yourset = {10,50,60,30}
print(yourset)

newset = myset.union(yourset)
print(newset)


print("difference",myset.difference(yourset))

## frozen set is also like the set btu here we cannot manipulate the data bcos it is immutable






