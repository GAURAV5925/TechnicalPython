e = int(input())
ep = set()
rno = map(int,input().split())

for i in rno:    
    ep.add(i)  #Here we are taking i as it will print from the 0th index
    
f = int(input())
fp = set()
rnof = map(int,input().split())

for i in rnof:    
    fp.add(i)
    
ns = ep.union(fp)

print(len(ns))
