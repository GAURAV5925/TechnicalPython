def print_rangoli(size):
    # your code goes here
    n = size
    
    l1 = list(map(chr,range(97,123)))
    
    x = l1[n-1::-1] + l1[1:n]
    #This will be complete length of the center element which will also be the longest element

    print(x)
    
    m = len('-'.join(x))
    
    for i in range(1,n):
        print('-'.join(l1[n-1:n-i:-1] + l1[n-i:n]).center(m,'-') )
     #    Here 1st we will join the two list in first it will be for 1st iteration e will be there nothing on left side and on Right Side e will be printed and will be aligned in the center 
     # 2nd iteration on Right side e on right side and d-e on right side then join will combine them and e-d-e will be formed 

     
        
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1] + l1[n-i:n]).center(m,'-') )


print_rangoli(5)
