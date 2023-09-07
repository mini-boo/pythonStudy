import sys


def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    #값이 1이면 소수 탈락
    if x==1 :
        return False
    #i = 2부터 값을 2로 나눈 몫에 +1한 것
    for i in range(2, x//2+1):
        #만약 x를 i로 나눈 나머지가 0이라면?
        if x & i == 0:
            return False
        else:
            return True


n=int(input())
a=list(map(input().split()))

for x in a:
    tmp=reverse(x)
    if isPrime(tmp) :
        print(tmp, end=' ')
