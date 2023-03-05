



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)**2)
    
    # Here the basic idea is that when we will take 
    # for i = 1 10//9=1 and 1**2 = 1
    # for i=2 100//9=11 and 11**2 == 121
    # and so on 
    # The basic idea is that here we are taking the sqaue of the 11,111,1111 and so on to obtain the result 
