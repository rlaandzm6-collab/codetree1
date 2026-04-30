a= []
#한줄에 한개씩 입력받으면 리스트어케만듦
cnt=0
cntcnt=0
for i in range(10):
    a=int(input())
    if a%3==0:
        cnt += 1
    if a%5==0:
        cntcnt +=1
print(cnt,cntcnt)

