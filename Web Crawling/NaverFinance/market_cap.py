import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page='
browser.get(url)

# 2. 조회 항목 초기화(체크되어 있는 항목 체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크된 상대이면
        checkbox.click() # 클릭(체크 해제)

# 3. 조회 항목 설정 (원하는 항목)
items_to_select = {'영업이익', '자산총계', '매출액'}
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') # 부모 elment
    label = parent.find_element(By.TAG_NAME, 'label') # label 모두 넣기
    if label.text in items_to_select: # label의 text가 items_to_select와 일치한다면
        checkbox.click() # 체크

# 4. 적용하기
button_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
button_apply.click() # 체크

for idx in range(1, 40): # 1~40까지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url + str(idx))

    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True) # 행전체가 비어있을경우 지움, 데이터프레임에 반영하기위해 inplace=True설정
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0: # 더 이상 가져올 데이터가 없으면
        break

    # 6. 파일저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): # f_name파일이 있다면 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
        # a 는 append
    else: # 파일이 없다면 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')
