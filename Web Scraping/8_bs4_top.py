import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=183559&page=1&sort=ASC&tab=mon"
res = requests.get(url)
res.raise_for_status() # 문제가 있을 시 바로 종료

soup = BeautifulSoup(res.text, "lxml") # html문서를 lxml을 통해 bs의 객체로 만듬
# print(soup)

cartoons = soup.find_all("nav", attrs={"class":"snb_nav"})
print(cartoons)

