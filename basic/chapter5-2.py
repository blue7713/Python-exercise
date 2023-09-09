# 사전 dictionary
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 값 출력
# print(cabinet[5]) # 없는 값 출력 시 오류, 실행 종료
print(cabinet.get(5)) # get을 부를 경우 없는 값에 대해 None 출력
print(cabinet.get(5, "사용 가능")) # None 대신 출력할 문장 

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 키에 대한 값을 변경
cabinet["C-20"] = "조세호" # 새로운 키와 값 추가
print(cabinet)

# 간 손님
del cabinet["A-3"] # 키 삭제
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# Key, Value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)