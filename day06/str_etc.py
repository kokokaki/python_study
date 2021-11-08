
# 대소문자 변환
s = 'GOOD Evening!! my name is KIM!'
print(s)
print(s.lower()) # 전부 소문자 변환
print(s.upper()) # 전부 대문자 변환
print(s.capitalize()) # 첫글자만 대문자 나머지 소문자

print('=' * 40)

'''
answer = input('사과의 영문 알파벳을 쓰세요! - ')

if answer.lower() == 'apple':
    print('정답입니다.')
else:
    print('틀렸습니다.')
'''

# 문자열 공백제거 함수 strip()
print('=' * 40)

user_id = '   abc1234 '
print(user_id.strip() == 'abc1234')

# 문자열 내부 단어 일괄교체: replace()

s2 = '파이썬 프로그래밍!!! 파이썬은 문자열 관련 함수가 많습니다.'

print(s2.replace('파이썬', 'python'))
print(s2.replace('!', ''))


