sentence = "나는 소년입니다"
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요"""
print(sentence3)

#슬라이싱
jumin = "990101-1234567"

print("성별 : " + jumin[7])
print("연 : "+ jumin[0:2])
print("월: " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : "+jumin[7:14])
print("뒤 7자리(뒤에부터) : "+jumin[-7:])

#문자열처리함수
python = "Python is amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[3].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)

print(python.find("n"))
print(python.find("Java"))
#print(python.index("Java")) : error

print(python.count("n"))

#문자열포맷
print("a" + "b")
print("a", "b")

#방법 1
print("나는 %d살입니다." % 20) #숫자
print("나는 %s을 좋아해요" % "파이썬") #문자열
print("Apple은 %c로 시작해요" % "A") #한 글자

#%s
print("나는 %s살입니다." % 20) #숫자, 정수 다
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법 3
print("나는 {age}살이며 {color}색을 좋아해요".format(age=20, color="빨간"))

#방법 4 (v3.6 이상~)
age = 20
color = "노란"

print(f"나는 {age}살이며 {color}색을 좋아해요")

#탈출문자
print("백문이 불여일견\n백견이 불여일타")

#\", \'는 문장 내에서 따옴표로 출력
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("C:\\PythonWorkspace")

# \r :커서를 맨 앞으로 이동
print("Red Apple\rpine")

# \b : 백스페이스 (한 글자 지우기)
print("Redd\bApple")

#\t : 탭 역할
print("Red\tApple")

#Q.
url = "http://naver.com"
my_str = url.replace("http://", "") #규칙 1
my_str = my_str[:my_str.index(".")] #규칙 2

password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
