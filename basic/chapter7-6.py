# 지역변수와 전역변수
gun = 10 # 전역변수

def checkpoint(soldiers): # 경계근무
    # gun = 10 # 지역 변수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

