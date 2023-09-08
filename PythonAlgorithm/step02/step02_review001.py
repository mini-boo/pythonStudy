import sys

n=int(input())
a = list(map(int, input().split()))
ave=round(sum(a)/n)
#ave=sum(a[:n-1])/n
min = 2176000000

for idx, i in range (n):
    ans = abs(i-ave)
    if ans < min:
        ans=min
        res = idx+1
        score = i
    if ans == min:
        if i>score:
            score = 1
            res = idx+1

print("{0} {1}".format(ave, res))