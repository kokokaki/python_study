

# 내장함수 len(): 순차형 자료의 내부 데이터 개수를 구함
# 문자열, 리스트, 튜플, 딕셔너리에서 공용사용가능함

s = 'python programming'
print('s의 글자수: {}개'.format(len(s)))


user_id = 'abc12355'

if len(user_id) < 8:
    print('id는 8글자 이상으로 쓰세요.')
else:
    print('사용 가능한 id입니다.')

p = [1,2,3,4,5, 100, 200, 300]
print(len(p))


'''
# 문자열 인덱스 탐색: find(), rfind()
- 문자열 내부의 특정 글자의 인덱스를 알려줌
- find는 앞글자부터 탐색, rfind는 뒷글자부터 탐색
- 탐색실패시 -1 반환
'''

# s = 'python programming'

print('=' * 40)
print(s.find('o'))
print(s.rfind('o'))

image_path = 'my_animal_dddddsjlfksjfldsjf.gif'

# 확장자 추출 - 맨 뒤에 있는 . 다음글자부터 끝까지 슬라이싱
ext = image_path[image_path.rfind('.') + 1 : ]
print(f'파일확장자: {ext}')

print('=' * 40)
print(s.find('강'))

user_pw = 'fff!1234'

if user_pw.find('!') == -1:
    print("비밀번호에 !를 넣어주세요")
else:
    print('사용가능한 패스워드입니다.')


# count(): 문자열 내부에 찾는 단어의 출현횟수를 반환
lyrics = '''
링딩동 링딩동 링디기링디기링딩동
링딩동 링딩동 링디기링디기링딩동
링딩동 링딩동 링디기링디기링딩동
링딩동 링딩동 링디기링디기링딩동
링딩동 링딩동 링디기링디기링딩동
'''

print(f'링딩동 반복횟수: {lyrics.count("링딩동")}회')

# 특정 문자가 문자열에 안에 포함되었는지의 유무만 확인

st = 'hello 안녕 내이름은 뽀로로야~'

print('=' * 40)

print('h' in st)
print('안녕' in st)
print('메롱' in st)
print('뽀로로' not in st)