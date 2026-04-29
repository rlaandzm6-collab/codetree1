N=int(input())


while N <=100:
    if N<60 :
        print("F",end=" ")
    elif N>=60 and N<70 :
        print("D",end=" ")
    elif N >=70 and N<80 :
        print("C",end=" ")
    elif N >=80 and N<90 :
        print("B",end=" ")
    elif N >= 90 and N<=100 :
        print("A",end=" ")
    N=N+1
