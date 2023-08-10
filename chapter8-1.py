# 표준 입출력
print("Python", "Java", "JavaScript", sep=",", end="?") # sep 구분문자, end 기본은 줄바꿈, 지정할 수 있음
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # 과목 : 왼쪽정렬 8자리 확보
    # 점수 : 오른쪽정렬 4자리 확보

# 은행 대기순번표
# 001 ,002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 빈공간 0으로 채우기, 3자리 확보

answer = input("아무 값이나 입력하세요 : ") # 입력받는 것은 항상 문자열형태로 저장되어짐
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")