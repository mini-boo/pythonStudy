# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) 
#     nums.append(int(input("두 번째 숫자를 입력하세요 : "))) 
#     nums.append(int(nums[0] / nums[1])) 
#     print("{0}/{1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러가 발생했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알 수 없는 오류가 발생했습니다.")


# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if nums >= 10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, num1/num2))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# class BigNumberError(Exception):
#     def __init__(self, msg) :
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if nums >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, num1/num2))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError:
#     print("에러가 발생했습니다. 한 자리 숫자만 입력해주세요.")
#     print(err)
# finally:
#     print("계산기를 이용해주셔서 감사합니다.")

#Q.
chicken = 10
waiting = 1

class SoldoutError(Exception):
   pass
    

while(True):
   try: 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken :
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldoutError
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldoutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

        
