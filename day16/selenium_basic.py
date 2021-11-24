

# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
from selenium import webdriver # 셀레늄 모듈 로딩
import time as t

# 크롬 브라우저 물리드라이버 가동
browser = webdriver.Chrome('D:/isec_spring1/py_study/c_driver/chromedriver.exe')

# 원하는 사이트로 이동
browser.get('https://www.naver.com')

# 자동으로 버튼이나 링크 클릭 제어하기
# login_btn = browser.find_element_by_css_selector('#account > a')
# login_btn.click()

# 자동으로 텍스트 입력하기
search = browser.find_element_by_css_selector('#query')
search.send_keys('멍멍이')

t.sleep(2)

# search_btn = browser.find_element_by_css_selector('#search_btn')
search_btn = browser.find_element_by_xpath('//*[@id="search_btn"]')
search_btn.click()



