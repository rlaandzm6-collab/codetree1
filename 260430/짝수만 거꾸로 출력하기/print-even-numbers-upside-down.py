A=int(input())
num=list(map(int,input().split()))
num=num[::-1]


for N in num:
    if N % 2 == 0:
        print(N,end=" ")
    


