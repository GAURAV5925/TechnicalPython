def print_formatted(number):
    
    w=len(str(bin(number))[2:])
    
    #Here we will take the Value as 5(For 2 Digit)/7(For 3 Digit Number) as we have to create a block of 5 elment for all the types and will give them the padding of another element
    
    for i in range(1,number+1):
        
        print(str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))
        #Here we will fill the alignment with space on left side and item will placed on right side

