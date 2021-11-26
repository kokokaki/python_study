
from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 파일입출력 내장함수 open은 웹데이터의 인코딩을 해석하지 못함
import codecs

# 날짜처리 라이브러리
from datetime import datetime

# 엑셀저장 라이브러리 
import xlsxwriter


# 오늘 날짜 시간 
d = datetime.today()

# 파일명
file_name = f'알라딘베스트셀러데이터_{d.year}_{d.month}_{d.day}.xlsx'

# 파일 저장 경로
file_save_path = f'D:/isec_spring1/py_study/{file_name}'

# 엑셀라이브러리 객체 생성
workbook = xlsxwriter.Workbook(file_save_path)

# 엑셀 워크 시트 만들기
worksheet = workbook.add_worksheet()

# 엑셀 열이름 (첫줄 정보 생성)
worksheet.write('A1', '순위')
worksheet.write('B1', '제목')
worksheet.write('C1', '저자')
worksheet.write('D1', '출판사')
worksheet.write('E1', '출판월')
worksheet.write('F1', '가격')


# 물리드라이버
browser = webdriver.Chrome('D:/isec_spring1/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
browser.maximize_window()

# 타겟 사이트로 이동
browser.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')


############ 핵심 로직 ###############
rank = 1

for n in range(2, 8):
    # 51위~ 100위: #newbg_body > div:nth-child(6) > ul > li:nth-child(3) > a
    # 101위 ~ 150위: #newbg_body > div:nth-child(6) > ul > li:nth-child(4) > a

    if n > 2: 
        # 순위 탭 클릭
        browser.find_element_by_css_selector(f'#newbg_body > div:nth-child(6) > ul > li:nth-child({n}) > a').click()

    t.sleep(1.5)

    # 현재 페이지 소스코드 불러오기
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')

    # 베스트 셀러 정보는 div.ss_book_box 에 있음
    # div_book_box_list = soup.select('div.ss_book_box')
    div_book_box_list = soup.find_all('div', class_='ss_book_box')


    for boox_box in div_book_box_list:
        div_book = boox_box.select_one('div.ss_book_list')
        # print(div_book)

        li_list = div_book.select('li')

        # 책 제목
        # 사은품이 있으면 1번, 없으면 0번
        if len(li_list) == 4:
            title = li_list[0].text
            info = li_list[1].text
            price = li_list[2].text
        else:
            title = li_list[1].text
            info = li_list[2].text
            price = li_list[3].text

        # info 세가지 데이터로 분해
        info_list =  info.split('|')
        author, company, pub_date = info_list

        # price에서 할인 후 가격만 추출
        price = price.split('(')[0]
        price = price[price.find('→') + 1 : ].strip()

        print(title)
        print(author.strip())
        print(company.strip())
        print(pub_date.strip())
        print(price)
        print('=' * 50)

        # 엑셀파일에 저장
        worksheet.write(f'A{rank+1}', rank)
        worksheet.write(f'B{rank+1}', title)
        worksheet.write(f'C{rank+1}', author)
        worksheet.write(f'D{rank+1}', company)
        worksheet.write(f'E{rank+1}', pub_date)
        worksheet.write(f'F{rank+1}', price)
        
        rank += 1

# 물리드라이버 종료
browser.close()
# 엑셀 워크북 종료(필수로해야 저장완료됨)
workbook.close()