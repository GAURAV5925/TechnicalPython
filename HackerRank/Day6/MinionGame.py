def minion_game(string):
    s1 = 0
    s2 = 0
    vow = "AEIOU"
    
    for i in range(len(string)):
        
        if string[i] not in vow: #If the vowel is not present then it will not start from first index
            
            s1 = s1 + (len(string)-i)  #Len would will be starting from that index to the last index means we can exclude the starting index as it will increase time complexity if we slice the index
        else:
            
            s2 = s2+(len(string)-i)  
    
    if s1>s2:
        
        print("Stuart",s1)
        
    elif s1<s2:
        
        print("Kevin",s2)
    else:
        
        print("Draw")
