from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 날짜처리 라이브러리
from datetime import datetime

# 엑셀저장 라이브러리 
import xlsxwriter

# 이미지 다운로드 처리 라이브러리
import urllib.request as req
from io import BytesIO



# 오늘 날짜 시간 
d = datetime.today()

# 파일명
file_name = f'멜론실시간차트순위_{d.year}_{d.month}_{d.day}.xlsx'

# 파일 저장 경로
file_save_path = f'D:/isec_spring1/py_study/{file_name}'

# 엑셀라이브러리 객체 생성
workbook = xlsxwriter.Workbook(file_save_path)

# 엑셀 워크 시트 만들기
worksheet = workbook.add_worksheet()

# 엑셀 열이름 (첫줄 정보 생성)

# 행 꾸미기
styles = {
    'bold': True,
    'font_color': 'red',
    'bg_color': 'yellow'
}
cell_format = workbook.add_format(styles)

'''
worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '썸네일', cell_format)
worksheet.write('C1', '가수명', cell_format)
worksheet.write('D1', '앨범명', cell_format)
worksheet.write('E1', '노래명', cell_format)
worksheet.write('F1', '좋아요수', cell_format)
'''

# 물리드라이버
browser = webdriver.Chrome('D:/isec_spring1/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
# browser.maximize_window()

# 브라우저 원하는 사이즈로 키우기
browser.set_window_size(1280, 1080)

# 타겟 사이트로 이동
browser.get('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79')

# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

best_list = soup.select('ul.list_type01 > li')

# print(f'개수: {len(best_list)}')
# print(best_list[0])

for book in best_list:

    # 타이틀 
    title = book.select_one('div.title').text.strip()
    # 저자
    author = book.select_one('div.author').text.strip()
    author_name_list = author.split('|')[0].split('저자 더보기')

    if len(author_name_list) == 1:
        main_author = author_name_list[0]
        sub_author = ''
    else:
        main_author, sub_author = author_name_list

    # 가격
    price = book.select_one('strong.book_price').text.strip()

    print(title)
    print(main_author.strip())
    print(sub_author.strip())
    print(price)

    print('=' * 60)