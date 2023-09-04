def open_account():
    [print("새로운 계정이 생성되었습니다.")]

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance > money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance-(money+commission)

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이고, 잔액은 {1}원입니다.".format(commission, balance))

#함수의 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이: {1}\t주 사용언어: {2}" \
          .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 30, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이: {1}\t주 사용언어: {2}" \
          .format(name, age, main_lang))
    
profile("김현수")

#키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", name = "김태호",  age=28)

#가변인자
def profile(name, age, *language):
        print("이름 : {0}\t나이: {1}\t".format(name, age), end="  ")
        for lang in language:
            print(lang, end="  ")
        print()

profile("유재석", 20, "Python", "Java", "C", "C++")
profile("김태호", 25, "Kotlin", "Swift")

# #지역변수와 전역변수

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

#Q.
def std_weight(height, gender):
    if gender =="man":
       return height*height*22
    else:
        return height*height*21

height = 175
gender = "man"
weight = round(std_weight(height/100, gender), 2)

print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height, gender, weight))