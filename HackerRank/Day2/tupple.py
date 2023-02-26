if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())      #Here we are converting the list into integer type
    print(hash(tuple(integer_list)))              #Hash will give the random value
