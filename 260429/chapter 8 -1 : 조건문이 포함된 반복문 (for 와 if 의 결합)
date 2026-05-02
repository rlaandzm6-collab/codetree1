# 🌲 오늘의 Codetree 학습 현황 🌲
chapter 8 -1 : 조건문이 포함된 반복문 (for 와 if 의 결합)
Q1. 
numbers = [10, 15, 20, 25, 30]
for num in numbers:
    if num % 2 == 0:
        print("짝수")
    elif num % 5 == 0:
        print("5의 배수인 홀수")
    else:
        print("기타")
A1. 
짝수
5의배수인 홀수
짝수
5의배수인 홀수
짝수

Q2.
험점수에 따라 등급을 정합니다.

90점 이상이면 A,
80점 이상이면 B,
70점 이상이면 C,
60점 이상이면 D,
60점 미만이면 F 라고 합니다.
첫번째 줄에 N 입력됨.
첫번째줄에 주어지는  N의 값부터100까지 공백을 두고 출력.
예시) (입력)85->(출력)BBBBBAAAAAAAAAA
A2.
n = int(input())

for i in range(n,101):
    if i >= 90 :
        print("A",end=" ")
    elif i >=80 :
        print("B",end=" ")
    elif i >= 70 :
        print("C",end=" ")
    elif i >= 60 : 
        print("D",end=" ")
    else :
        print("F",end="")

Q3.
짝수만 거꾸로 출력하기
N 개의 정수가 주어집니다.
주어진 정수 중에서 짝수만 출력하는 프로그램을 작성해보세요. 이때, 입력에서 주어진 순서의 역순으로 짝수만 출력해야 합니다.
예를 들어, N=6 개의 정수가 3, 1, 4, 5, 6, 2 순으로 주어졌다면, 2, 6, 4를 차례대로 출력해야 합니다.
(입력)첫줄에 정수 N이 입력됨. 다음줄에 N개의 정수가 차례대로 공백으로 구분되어 주어짐.
예시) 
(입력)
6
3 1 4 5 6 2
(출력) 2 6 4
A3.
A=int(input())
num=list(map(int,input().split()))

for N in range(A-1,-1,-1):
    if num[N] % 2 == 0:
        print(num[N],end=" ")





주어지는 점수 N부터 100점까지 1점씩 증가하며 각 점수가 어떤 등급에 해당하는지 출력하는 프로그램을 작성해보세요.

