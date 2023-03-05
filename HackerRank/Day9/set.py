def average(array):
    new_arr = set(array)
    
    new_arr = list(new_arr)
    sum = 0
    for i in range(len(new_arr)):
        sum += new_arr[i]
    
    avg = sum / len(new_arr)
    
    return round(avg,2)

