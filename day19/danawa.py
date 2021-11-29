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
file_name = f'애플노트북인기순위_{d.year}_{d.month}_{d.day}.xlsx'

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
browser.get('http://prod.danawa.com/list/?cate=112758')



######### 핵심 로직 ###########


# 제조사별 더보기 링크 클릭
t.sleep(2)
browser.find_element_by_css_selector('#dlMaker_simple > dd > div.spec_opt_view > button.btn_spec_view.btn_view_more').click()

# 애플 체크박스 클릭
t.sleep(1.5)
browser.find_element_by_css_selector('#searchMaker1452').click()

t.sleep(3)

# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

# 메인 상품 리스트 가져오기
prod_list = soup.select('.main_prodlist > ul > li.prod_item')

for i in range(30):

    p = prod_list[i]

    # 모델명
    prod_name = p.select_one('p.prod_name > a').text.strip()

    # 가격
    prod_price = p.select_one('p.price_sect > a').text.strip()

    print(prod_name)
    print(prod_price)
    print('=' * 60)
    