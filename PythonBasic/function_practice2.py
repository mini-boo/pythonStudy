#내장함수

#input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random #외장 함수
print(dir())

print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

#외장함수
# glob : 어떤 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob("*.py"))

#os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 파일입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())

#time: 시간 관련 함수들
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)