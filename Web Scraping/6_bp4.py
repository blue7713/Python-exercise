import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status() # 문제가 있을 시 바로 종료

soup = BeautifulSoup(res.text, "lxml") # html문서를 lxml을 통해 bs의 객체로 만듬
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 객체에서 첫 번쨰로 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 처음으로 발견되는 a tag에 해당하는 class의 속성이 Nbtn인 속성만 찾음
print(soup.find(attrs={"class":"Nbtn_upload"})) # class = "Nbtn" 인 어떤 element를 찾아줘

rank1 = soup.find("li", attrs={"class":"AsideList__item--i30ly"}) # class = AsideList__item--i30ly인 li tag를 찾아줘
print(rank1)
# print(rank1.a.get_text)
# print(rank1.next_sibling) # 형제 관계의 태그 출력
# print(rank1.parent) # rank1의 부모 태그 출력
rank1.find_next_sibling("li") # rank1 기준으로 li 태그인 형제만 출력
# print(rank1.get_text)
rank1.find_next_siblings("li") # rank1 기준으로 li 태그인 형제들을 모두 출력

