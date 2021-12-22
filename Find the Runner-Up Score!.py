if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a= sorted(arr)
    a1= set(a)
    a1.remove(max(a1))
    print(max(a1))
    #for i in range(0, len(a)):
        #b= max(a)
