#최솟값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 4]

#float('inf')는 파이썬에서 무한대를 나타내는 부동소수점 숫자. 어떤 숫자와 비교해도 항상 크다는 것을 의미
arrMin=float('inf')

for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]

print(arrMin)