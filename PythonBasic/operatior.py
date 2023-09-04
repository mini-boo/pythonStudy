print(1+1)
print(3-1)
print(5*2)
print(6/3)

print(2**3) #2^3
print(5%3) #나머지
print(10%3)
print(5//3) #몫
print(10//3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

#값 비교
print(3 == 3)
print(4==2)
print ( 3+4 == 7)

#부정
print (1 != 3)
print(not(1 != 3))

#And
print((3>0) and (3<5))
print((3>0) & (3<5))

#or
print((3>0) or (3>5))
print((3>0) | (3>5))
print (5>4>3)

#변수 적용
print(2+3*4)
print((2+3)*4)

number = 2+3*4
print(number)

number = number + 2
print(number)

number += 2
print(number)

number *= 2
print(number)

number /= 2
print(number)

number -= 10
print(number)

number %= 3
print(number)

#숫자처리 함수
print(abs(-2)) #절댓값
print(pow(4, 2)) #4^2
print(max(2, 5))
print(min(2, 5))
print(round(3.14)) #반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

#랜덤함수
from random import *
print(random()) #0.0 이상 1.0 미만 임의의 값을 생성
print(random()*10) #0.0이상 10.0 미만 임의의 값 생성
print(int(random()*10))

print(int(random()*45) +1)

print(randrange(1, 46)) #1~45 까지 숫자 중 랜덤 하나 출력
print(randint(1, 45))

#Q.
from random import *
date = randint(4, 28)
print("오프라인 스터디 모집 날짜는 매월 " + str(date)+"일로 선정되었습니다.")