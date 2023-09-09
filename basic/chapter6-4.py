# continue와 break
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1부터 10까지
    if student in absent:
        continue # 아래의 코드를 실행하지 않고 다음 순번 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 뒤의 반복문 실행 x, 탈출
    print("{0}, 책을 읽어봐".format(student))