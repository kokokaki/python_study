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

worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '썸네일', cell_format)
worksheet.write('C1', '가수명', cell_format)
worksheet.write('D1', '앨범명', cell_format)
worksheet.write('E1', '노래명', cell_format)
worksheet.write('F1', '좋아요수', cell_format)


# 물리드라이버
browser = webdriver.Chrome('D:/isec_spring1/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
# browser.maximize_window()

# 브라우저 원하는 사이즈로 키우기
browser.set_window_size(1280, 1080)

# 타겟 사이트로 이동
browser.get('https://www.melon.com/chart/index.htm')

# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

######### 핵심 로직 ###########

tr_list1 = soup.find_all('tr', class_='lst50')
tr_list2 = soup.find_all('tr', class_='lst100')

tr_list = tr_list1 + tr_list2

for song in tr_list:
    rank = int(song.select_one('.rank').text.strip())
    title = song.select_one('.rank01').text.strip()
    artist = song.select_one('.rank02 > a').text.strip()
    album = song.select_one('.rank03').text.strip()
    like = song.select_one('.cnt').text.strip()
    like = like[3:].strip()

    img_tag = song.select_one('.image_typeAll > img')
    img_src = img_tag['src']

    print(f'순위: {rank}')
    print(title)
    print(artist)
    print(album)
    print(like)
    print(img_src)

    # 엑셀에 데이터 저장
    worksheet.write(f'A{rank+1}', rank)

    # 엑셀에 이미지 저장
    # worksheet.write('B1', '썸네일')
    # 이미지경로를 통해 이미지 다운
    img_data = BytesIO(req.urlopen(img_src).read())
    worksheet.insert_image(f'B{rank+1}', img_src, {'image_data': img_data})

    worksheet.write(f'C{rank+1}', artist)
    worksheet.write(f'D{rank+1}', album)
    worksheet.write(f'E{rank+1}', title)
    worksheet.write(f'F{rank+1}', like)

browser.close()
workbook.close()
