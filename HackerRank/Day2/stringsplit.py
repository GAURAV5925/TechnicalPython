def split_and_join(line):
    a = line.split()
    b = "-".join(a)  #Here in place of the space "-" will be printed using the join function
    
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
