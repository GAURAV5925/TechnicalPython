from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    first = dt.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    second = dt.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    
    # Refer here to know more https://www.w3schools.com/python/python_datetime.asp
    
    return str(abs(int((first-second).total_seconds())))
    # Here we are subtracting first time from second and taking the total seconds using the total_seconds() function then converting it into int and rounding off by abs and converting it into str
    
