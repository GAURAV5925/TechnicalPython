def merge_the_tools(string, k):
    
    ss = []
    i = 0
    
    # ss --> sub string
    
    #len(string)//k --> It is the the total no of sub string we can form from the string
    
    for j in range(len(string)//k):
        ss.append(string[i:i+k])
        i=i+k
    
    #fss --> final sub string
        
    for fss in ss:
        print("".join(list(dict.fromkeys(list(fss)).keys())))
        # list(fss) will break the sub string in single char
        # then we will allote the single character as the key to the dict
        # then we will fetch that key value
        # convert it into the list
        # by using the join we will make it the sub string without any repition of the word
            
        
   
