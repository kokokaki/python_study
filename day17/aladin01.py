
from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 물리드라이버
browser = webdriver.Chrome('D:/isec_spring1/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
browser.maximize_window()

# 타겟 사이트로 이동
browser.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

############ 핵심 로직 ###############

# 베스트 셀러 정보는 div.ss_book_box 에 있음
# div_book_box_list = soup.select('div.ss_book_box')
div_book_box_list = soup.find_all('div', class_='ss_book_box')

# print(div_book_box_list[0])


for boox_box in div_book_box_list:
    div_book = boox_box.select_one('div.ss_book_list')
    # print(div_book)

    li_list = div_book.select('li')

    # 책 제목
    # 사은품이 있으면 1번, 없으면 0번
    if len(li_list) == 4:
        title = li_list[0].text
        info = li_list[1].text
    else:
        title = li_list[1].text
        info = li_list[2].text

    # info 세가지 데이터로 분해
    info_list =  info.split('|')
    author, company, pub_date = info_list

    print(title)
    print(author.strip())
    print(company.strip())
    print(pub_date.strip())
    print('=' * 50)

