new_list = list(map(int,input().split()))

cnt=0
for i in range(new_list[0],new_list[1]+1):
    if i %2==1 :
        continue
    cnt = cnt+i
print(cnt)