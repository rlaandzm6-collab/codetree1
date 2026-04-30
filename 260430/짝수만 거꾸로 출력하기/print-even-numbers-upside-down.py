A=int(input())
num=list(map(int,input().split()))



for N in range(A-1,-1,-1):
    if num[N] % 2 == 0:
        print(N,end=" ")
    


