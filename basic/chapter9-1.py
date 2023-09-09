# 클래스, 스타크래프트
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
class Unit:
    def __init__(self, name, hp, damage): # __init__ : 생성자
        self.name = name # 멤버변수, 클래스 내에서 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼았음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

# class가 아닌 외부에서 만든 것
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))