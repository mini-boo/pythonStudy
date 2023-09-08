c=map(int, input())

for i in range(c):
    li = list(map(int, input().split()))
    cnt = 0
    for j in li[1:]:
        ave=sum(li[1:])/li[0]
        cnt += 1
    rate = cnt / li[0] * 100
    print('{0:0.3f}%'.format(rate))