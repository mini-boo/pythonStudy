#리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번째 칸에 타고 있나?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석씨와 조세호씨 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5, 3, 2, 4, 1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우고 싶을 때
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [5, 3, 2, 4, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)

#딕셔너리
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)

#새손님
cabinet["c"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["c"]
print(cabinet)

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name="김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)

#세트(집합)
# 중복이 안 됨, 순서가 없음

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합(자바는 할 수 있지만 파이썬은 할 줄 모름)
print(java - python)
print(java.difference(python))

#파이썬 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹었음
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

#Q.

from random import *
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = range(1, 21)
lst = list(lst)
shuffle(lst)

print("--당첨자 발표--")
print("치킨 당첨자 : " + str(sample(lst, 1)))
print("커피 당첨자 : " + str(sample(lst, 3)))
print("--축하합니다--")

winners = sample(lst, 4)

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("치킨 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")