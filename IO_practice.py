print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", sep=",", file=sys.stdout) #표준 출력
# print("Python", "Java", sep=",", file=sys.stderr) #에러 처리

#시험 성적
scores = {"수학":0, "영어": 50, "코딩": 100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4))

#은행 대기 순번표
# 001, 002, 003, ...

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 :")
# print("입력하신 값은 " + answer + "입니다.")

#출력포맷

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

#양수일 때는 +표시, 음수일 땐 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬하고, 빈칸을 _로 채우기
print("{0:_<+10}".format(500))

#3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000000))

#3자리마다 콤마 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000000))
print("{0:+,}".format(-1000000000000000))

#3자리 마다 콤마 찍어주기, 부호도 붙이고, 자리수도 확보해보기
#돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000000000))

#소수점 출력
print("{0:f}".format(5/3))

#특정 자리수까지만 표시하고 싶어
print("{0:.2f}".format(5/3))

#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 80")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")

score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

#pickles

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #프로필에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#with

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "rb") as study_file:
#     print(study_file.read())

#Q.
for i in range(1:51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

