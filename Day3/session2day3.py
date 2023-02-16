'''a=int(input())
a=int(input("enter a number"))
a=input("enter a number")

print(a)'''

# code for FIBONACCI SERIES(code by sir)

'''n = int(input("Enter the number"))
a=0
b=1
count=0



while(count<n):
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
'''

'''for iterator in range(start,end,step):
    statements
    
    
    if Steps are not give it will increase by default 1'''


#This code will print 2's Table

'''
for i in range(1,11): #Here Range the start are inclusive and end are exlusive meaning From 1 to 10
    print(i*2)
'''

'''
mylist=[3,5,6,8,2] #This will print the whole list
for i in mylist:
    print(i)



tuple=(3,"Gaurav",6.25,"85",2) #This will print the whole tuple
for i in tuple:
    print(i)


name="Gaurav" #This will print the whole string
for i in name:
    print(i)


for i in name: #This will find the letter which 
    if i=="a":
       print(i)



for i in range(1,11,2): #This will print alternate no's starting from 1 till 10
    print(i)



for i in range(10,0,-1): #This will print reverse no's starting from 10 till 9
    print(i)


r = range(30,5,-2)
for i in r:
    print(i)'''


'''for i in range(1,101,1):
     print("I will study seriously")'''


## Code for FInding the vowels in the STRING

'''
n = "gaurav"
n = n.lower()
count = 0

for i in range(0,6):  ##Here using range is compulsory as character will be comapred in place of index which is in int format
    print(n[i])
    if n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u":
        count = count + 1
    
print(count)'''




#NESTED FOR LOOP

'''for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")'''





#Break will terminate the complete loop and no further iteration will be possible
#Pass will just skip one step not all the loop.
#Continue will skip all the loop and will execute the next iteration

'''for i in range(1,10):
    print(i)
    if i==5:
        break  #This line will terminate the loop no further iteration after 5


for i in range(1,10):
    print(i)
    if i==5:
        pass
    print(i)'''


'''
a = eval(input("Enter the expression"))
sum = 0
for x in a:
    sum=sum+x
print(sum)
'''


for i in range(1,5):
    if(i==3):
        break
print("----------")



s = "My Name is Gaurav"
print(s.find("Gaurav"))  #This will give the index no on which the given Word start
print(s.find("Name"))








