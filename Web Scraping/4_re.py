import re # 정규식 라이브러리 호출

p = re.compile("ca.e") # 정규식 사용 # p : pattern

# . (ca.e): 하나의 문자 의미 > care, cafe, case | caffe(x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade(x)
# $ (se%) : 문자열의 끝 > case, base (o) | face(x)

def print_match(m):
    if bool(m) == True: # 매치되면 출력
        print("m.group:",m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else: # 매치되지 않으면 출력
        print("매칭되지 않음")

# m = p.match("case")
m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
# print(m.group()) 
# 정규식과 매치 되면 출력, 매치되지 않으면 에러 

m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall("careless") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e): 하나의 문자 의미 > care, cafe, case | caffe(x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade(x)
# $ (se%) : 문자열의 끝 > case, base (o) | face(x)
