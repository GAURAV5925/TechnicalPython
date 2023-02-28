def count_substring(string, sub_string):
    
    count = 0
    l = len(sub_string)    #Taking len of the substring to use it slicing in further code
    
    for i in range(len(string)):
        s=string[i:i+l]  #Here we will take sub string and move ahead For Eg. ABCDACDA  1ST--> ABC 2ND --> BCA and so on
        if s == sub_string: #Comparing the substring with our string which will move ahead with each iteration
            count += 1     #When the condition will satisfied count will increase
    
    return count
