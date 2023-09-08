import sys

n = map(int, input())
a = list(map(int, input().split()))
ave=round(sum(a)/n)
min=2147000000

#인덱스값과 점수 짝지어서 돌리기
for idx, i in enumerate(a):
    #tmp = 값과 평균 간 거리(절댓값)
    tmp = abs(i-ave)
    #tmp가 모종의 수(min)보다 작으면 tmp가 min이 되고 점수도 i가 됨, 학생번호는 인덱스+1
    if tmp<min:
        min=tmp
        score = i
        res = idx+1
    #tmp와 min이 같고, 점수가 기존 score보다 크면 값 바꾸기
    elif tmp==min:
       if i>score:
           score = i 
           res = idx+1

print(ave, res)