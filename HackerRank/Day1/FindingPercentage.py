if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for m in range(n):
        name, *line = input().split()    # *line will make the imput in same line but after the space it will taken in the list as a string
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    
    print(format(sum(marks)/3,'.2f'))  #SYNTAX --> fromat(value,'.nf')   .nf is in the string format
    
    #This formate will make the float value upto 2 digit
