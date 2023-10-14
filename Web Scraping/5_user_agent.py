import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"}
res = requests.get(url, headers=headers) 
res.raise_for_status() 
with open("nadocoding.html", "w", encoding="utf8") as f: # html정보를 파일로 만듬
    f.write(res.text)

