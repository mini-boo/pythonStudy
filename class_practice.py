# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음.
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{0}유닛이 생성되었습니다.".format(name))
print("체력 : {0} 공격력 : {1}".format(hp, damage))

#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0}유닛이 생성되었습니다.".format(tank_name))
print("체력 : {0} 공격력 : {1}".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} 유닛이 {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 : {0} 공격력 : {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
# marine3 = Unit("마린") > 변수가 모두 없으면 사용 불가

#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)

print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name, wraith1.hp))


#멤버변수
#마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))


#메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage 
    
    def attact(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}가 파괴되었습니다.".format(self.name))

#파이어뱃  : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이어캣", 50, 16)
firebat1.attact("5시")

firebat1.damaged(25)

#상속

class Unit2:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

class AttackUnit2(Unit2):
    def __init__(self, name, hp, damage):
        Unit2.__init__(self, name, hp)
        self.damage = damage

#다중상속
#드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도: {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttactUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkirie = FlyableAttactUnit("발키리", 200, 6, 5)
valkirie.fly(valkirie.name, "2시")

#메서드 오버라이딩
class Unit3:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
    def fly(self, location):
        print("[공중 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


#배틀크루저
battlecruiser = Unit3("배틀크루저", 500 , 3)

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, damage):
        pass

#서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, 5)

def game_start():
    print("[알림] : 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#super
class BuildingUnit2(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.damage = location