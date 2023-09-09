# 세트 (set) 
# 중복x, 순서x
my_set = {1, 2, 3, 3, 3} # 중복부분은 무시
print(my_set)

Java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (Java 와 Python을 모두 할 수 있는 개발자)
print(Java & python)
print(Java.intersection(python))

# 합집합 (Java 도 할 수 있거나 python 할 수 있는 개발자)
print(Java | python)
print(Java.union(python))

# 차집합 (Java는 할 수 있지만 python을 할 줄 모르는 개발자)
print(Java - python)
print(Java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
Java.remove("김태호")
print(Java)