e = int(input())
ep = map(int,input().split())
rno = set()

for i in ep:
    rno.add(i)
    
f= int(input())
fp = map(int,input().split())
frno = set()

for i in fp:
    frno.add(i)
    
x = rno.difference(frno)



print(len(x))
