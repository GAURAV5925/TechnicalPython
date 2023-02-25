if __name__ == '__main__':
    res=[]
    grade=[]
    for n in range(int(input())):
        name = input()
        score = float(input())
        res.append([name,score])
        grade.append(score)
        
grades = sorted(set(grade))
m = grades[1]

name = []

for val in res:
    if m == val[1]:
        name.append(val[0])
        
name.sort()

for i in name:
    print(i)

