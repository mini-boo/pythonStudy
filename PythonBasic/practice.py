#숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자형
print('풍선')
print("나비")
print("지나가버린"+" 어린시절에")
print("ㅋ"*9)

#참, 거짓
print(5>10)
print(5<10)
print(True)
print(not False)
print(not (5>10))

#반려동물을 소개해주세요

animal = "고양이"
name = "해피"
age = 1
hobby = "낮잠"
is_adult = age >=3

print("우리집" + animal + "의 이름은 " + name + "에요.")

hobby = "공놀이"

#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")

#콤마(,)를 쓰면 띄어쓰기가 하나씩 들어감
print(name, "는 ", age, "살이며, ", hobby,"을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))


'''
이렇게 하면 주석도 됩니다
'''


#Q.
station = "사당"

print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"

print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"

print(station + "행 열차가 들어오고 있습니다.")