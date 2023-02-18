def arm(value,dig1):

    value1=value
    dig_sum = 0
    flag = True
    


    while value>0:
        
        rem=value%10   #

        dig_cub = rem**dig1  # Cube of the digit
        dig_sum = dig_cub + dig_sum   # Previous value will be added
        value = value//10  # We will eliminate last digit

    if value1==dig_sum:
           flag = False


    if flag==False:
        print("Armstrong Number")
            
    else:
        print("Not a Armstrong Number")
            

num = int(input("Enter the number"))
# typecast = str(num)
# dig = len(typecast)

count = 0
while num > 0:
    num=num//10
    count = count+1


print(count)


arm(num,count)
