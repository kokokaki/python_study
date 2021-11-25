
# 뷰티풀 숩: html 소스코드를 분해하여 필요한 정보를 걸러내주는 라이브러리
from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <meta charset="utf-8">
        <title>Nana World</title>
    </head>
    <body>
        <h1>Welcome To My World</h1>
        <h2>여기는 나나월드</h2>
        <b>안녕안녕</b>
        <p class="title">
            <b>Here you are</b>
        </p>
        <p class="content">
            이 곳에는 여러 사람들이 살고 있습니다.
            <a href="http://www.nanaworld.com/nana" class="family" id="link1">Nana</a>
            <a href="http://www.nanaworld.com/nono" class="family" id="link2">Nono</a>
            <a href="http://www.nanaworld.com/nini" class="friend" id="link3">Nini</a>
        </p>
        <p class="content">
            blah blah~......
        </p>
    </body>
</html>
'''


# 1. 뷰티풀 숩 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 2. 내용 확인
print(soup.prettify())

# 3. 중요! 원하는 태그 추출 find, find_all
b_tag = soup.find('b')
print(f'b_tag: {b_tag}')

h1_tag = soup.find('h1')
print(f'h1_tag: {h1_tag}')

# 위에서부터 처음발견된 a를 가져옴
a_tag = soup.find('a')
print(f'a_tag: {a_tag}')

# a태그중 원하는 태그 특정하기
print('=' * 40)
a_nono_tag = soup.find('a', id='link2')
print(f'a_nono_tag: {a_nono_tag}')

a_nini_tag = soup.find('a', class_='friend')
print(f'a_nini_tag: {a_nini_tag}')

# 태그에서 텍스트 추출
nini_text = a_nini_tag.text
print(f'nini_text: {nini_text}')

# 태그에서 속성값 추출
nono_link = a_nono_tag['href']
print(f'nono_link: {nono_link}')

# 다중 조건
nana_tag = soup.find('a', id='link1', class_='family')
print(f'nana_tag: {nana_tag}')

print('='*40)
p_title = soup.find('p', class_='title')
print(f'p_title: {p_title}')

b_tag = p_title.find('b')
print(b_tag.text)

# 여러 개를 가져올 때는 find_all
print('=' * 40)
p_content_list = soup.find_all('p', class_='content')
print(p_content_list)

print('=' * 40)
print(p_content_list[1].text.strip().replace('~', '!'))


#####################################################

# select_one, select
# css 선택자 문법으로 태그를 지목하는 방법

# css 선택자 예시 ( # : 아이디,  . : 클래스 , > : 자식 )

# a 태그이면서 클래스 이름이 banana  ->    a.banana
# div태그이면서 아이디가 user   ->  div#user
# p태그의 자식 a태그인데 a의 아이디가 num   ->  p > a#num

print('=' * 40)
ex1 = soup.select_one('.title > b')
print(ex1.text)

ex2 = soup.select_one('#link3')
print(ex2.text)

ex3 = soup.select_one('p.content > a.friend')
print(ex3.text)

