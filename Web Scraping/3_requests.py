import requests
res = requests.get("http://naver.com") # url을 받아옴
res.raise_for_status() # 올바른 HTML을 가져왔다면 정상작동, 잘못된 HTML이라면 에러
print("응답코드 :", res.status_code) # 200 이면 정상


if res.status_code == requests.codes.ok: # status_code가 200이면
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# 결론 # 세트로 쓰기
res = requests.get("http://google.com")
res.raise_for_status()

print(len(res.text))
print(res.text)

# with open("mynaver.html", "w", encoding="utf8") as f: # html정보를 파일로 만듬
#     f.write(res.text)