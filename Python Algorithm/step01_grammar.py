#변수 정하기
A = 1
B = 2
print(A, B)

a, b, c = 1, 2, 3
print(a, b, c)

#값 교환
a, b = 10, 20
print(a)
a, b=b, a 
print(a)

#변수 타입
a=12345
print(type(a))

print(a, b, c, sep=",")
print(a, end='  ')

#변수 입력과 연산자
# a, b = input("숫자를 입력하세요 ").split()
# print(type(a))
# a=int(a)
# b=int(b)
# c=a+b 
# print(type(c))
# print(c)

#조건문

x = 7

if x==7:
    print("lucky")

if x>=10:
    if x%2==1:
        print("lucky")
    else:
        print("엥")
else:
    print("아닌데")

#반복문(for, while)
a=range(1, 11)
print(list(a))

# for i in range(10):
#     print("hello")

i=10

while i<=10:
    print(i)
    i=i-1
    if i==0:
        break

n=int(input("입력하세요 : "))
sum = 0
# for i in range(1, n+1):
#     print((i*2)-1)

# for i in range(1, n+1):
#     sum = sum+i
# print(sum)

for i in range(1, n+1):
    if n%i == 0:
        print(i)

#이중 for문
for i in range(5):
    for j in range(5):
        print("*", end="\n")

#문자열과 내장함수
msg= "It is Time"

for x in msg:
    if x.isupper():
        print(x, end="  ")

#ord: 아스키 넘버 (대문자 A~Z까지 매겨진 숫자)
#isalpha: 문자열의 구성이 알파벳인지에 대해서 확인하는 방법

#리스트와 내장함수

import random as r

a=[]
print(a)
b=list()

#append : 리스트의 끝에 새로운 요소를 추가하는 메소드, insert(인덱스 번호, 넣을 값)
#pop : 끝에 있는 값을 리스트에서 제거한다. (인덱스 번호, 버릴 값)
#remove(없앨 값)
#index(찾을 값)
#sort(reverse=True) : 내림차순
#sort : 오름차순
#for x in enumerate(튜플로 하나하나 짝지어줌 (인덱스 번호, 값))
#if all(60>x for x in a): > 조건이 모두 참일 경우 조건문