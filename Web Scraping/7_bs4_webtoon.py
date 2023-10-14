import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status() # 문제가 있을 시 바로 종료

soup = BeautifulSoup(res.text, "lxml") # html문서를 lxml을 통해 bs의 객체로 만듬
# print(soup)

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":""})
# class 속성이 contentTitle인 모든 a 태그 속성 가져오기
for cartoon in cartoons:
    print(cartoon.get_text())