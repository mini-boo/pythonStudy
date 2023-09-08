import sys

n, k = map(int, input().split())
a=list(map(int, input().split))
res=set() #중복제거

#숫자 세 개 뽑기
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

#리스트화
res = list(res)

#내림차순 정렬
res.sort(reverse=True)
print(res[k-1])
