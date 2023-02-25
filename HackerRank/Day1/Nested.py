if __name__ == '__main__':
    res=[]
    grade=[]
    for n in range(int(input())):
        name = input()
        score = float(input())
        res.append([name,score])   #Here we are creating a list inside a list in which we are storing the value of the name and score
        grade.append(score)      #We are creating a another list in which we are storing the scores
        
grades = sorted(set(grade))  #Sorted can be used to sort all LIST / DICT/ TUPLE
m = grades[1]             #Here we have assigned the value of second lowest score to the variable m

name = []

for val in res:
    if m == val[1]:
        name.append(val[0])    #Here we are acessing the list with val and using the index we are accessing the name and appending it into the name list
        
name.sort()    #Sort is only for the list Type

for i in name:
    print(i)

