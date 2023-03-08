e= int(input())
rno = map(int,input().split())
ep = set()

for i in rno:
    ep.add(i)

f= int(input())
frno = map(int,input().split())
fp = set()
    
for i in frno:
    fp.add(i)
    
res = fp.symmetric_difference(ep)

print(len(res))
