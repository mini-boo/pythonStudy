import sys

n, m = map(int, input().split())
#변수 선언을 통해 카운트 될 공간 만들기
cnt=[0]*(n+m+3)
max = 0

#i, j중에 하나씩 골라 더해서 카운트 하기
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

#최댓값일 경우 값 바꾸기
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]

#프린트하기
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')