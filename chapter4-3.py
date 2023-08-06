# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 전체를 소문자로 
print(python.upper()) # 전체를 대문자로
print(python[0].isupper()) # 대문자인지 반환
print(len(python)) # 문자열의 길이 반환
print(python.replace("Python", "Java")) # 문자열 교체

index = python.index("n") # 첫번째 n글자의 인덱스 반환
print(index)
index = python.index("n", index + 1) # 시작위치 지정, 두 번째 n글자의 인덱스 반환
print(index)

print(python.find("Java")) # 원하는 값이 없을 때 -1 반환
#print(python.index("Java")) # 원하는 값이 없을 때 에러

print(python.count("n"))