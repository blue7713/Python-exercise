# 가변인자
def profile(name, age, *language): # * = 가변인자 선언
    print("이름 : {0}\t나이 : {1}\t". format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")