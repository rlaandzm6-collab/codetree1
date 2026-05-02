a= ["apple","banana","grape","blueberry","orange"]
cnt=0
W=input()

for i in range(5):
    if a[i][2] == W:
        cnt += 1
        print(a[i])
    elif a[i][3] ==W:
        cnt+=1
        print(a[i])
print(cnt) 