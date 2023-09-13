n=int(input())

for i in range(n):
    a=int(input())
    size=len(a)
    for j in range (size//2):
        if a[j]!=a[-j-1]:
            print(0)
        else:
            print(1)