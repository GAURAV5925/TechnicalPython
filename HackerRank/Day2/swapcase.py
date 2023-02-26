def swap_case(s):
    x=""
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        x+="".join(i)
    
    return x
