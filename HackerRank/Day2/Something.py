if __name__ == '__main__':
    N = int(input())        #Taking the no of commands to be executed
    
    lis=[]    #Intialising the list
    
    for i in range(N):
        cmd = input().split()     #Taking the commands and values
        
        if cmd[0]=='insert':
            lis.insert(int(cmd[1]),int(cmd[2]))     #Here we are converting the CMD List value as they where stored in the string format
        elif cmd[0]=='print':
            print(lis)
        elif cmd[0]=='remove':
            lis.remove(int(cmd[1]))
        elif cmd[0]=='append':
            lis.append(int(cmd[1]))
        elif cmd[0]=='sort':
            lis.sort()
        elif cmd[0]=='pop':
            lis.pop()
        else:
            lis.reverse()
 
