'''
IN THE LIST COMPREHENSION WE CAN USE THE FOR LOOP INSIDE THE LIST ITSELF
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x1 = [p for p in range(x+1)]  #Here we are calculating the no of possibility of x for eg. 2 --> 0,1,2
    y1 = [q for q in range(y+1)]
    z1 = [r for r in range(z+1)]
    
    per = [[i,j,k] for i in x1 for j in y1 for k in z1]    #Here we are arranging them in the permutation form
    
    req = [ l for l in per if sum(l)!=n]    #Here we are checking waether there sum is equal to n of the per LIST
    
    print(req)
