#2nd Day - Data types in python are Dynamically Typed hence we not need to specify the Data types like in other language.


#String Operation
name = "Gaurav"
#Indexing 0 1 2 3 4 5
#Negative Indexing -1 -2 -3 -4 -5 -6

#String slicing name[start:end:steps]
#Note : start is inclusive meaning that index will be included and end are exclusive meaning that index will not be included hence consider a no+1 for the target index

print(name[0])
print(name[-1]) #negative indexing

print(name[0:7:2]) #For skipping the nos use 2 for alternative and 1 is default it will include all the number

print(name[0:7:1]) #Complete name will be printed

print(name[0:])#default values for ennd will print complete string

print (name[:7])#default start value will start from 0th index and end on last index

