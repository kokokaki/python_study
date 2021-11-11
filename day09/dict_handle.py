
eng_kor = {'student':'학생', 'peach':'복숭아', 'book':'책'}
print(eng_kor)

# 딕셔너리에 데이터 추가
# - 저장되어있지 않은 key를 이용해서 데이터를 대입
eng_kor['grape'] = '포도'
print(eng_kor)

# 딕셔너리에 데이터 수정
# - 저장되어 있는 key를 이용해서 데이터 대입
eng_kor['book'] = '서적'
print(eng_kor)

# 딕셔너리 내부 데이터 삭제
del(eng_kor['student'])
print(eng_kor)

print('=' * 40)

# keys(), values()함수를 쓰면 키목록과 값목록을 얻을 수 있음
print(eng_kor.keys())
print(eng_kor.values())

# 딕셔너리의 반복문 처리
# key를 뽑아서 반복함
print('=' * 40)
for k in eng_kor:
    print(eng_kor[k])


# 빈 사전 만들기
empty_dict = {}
empty_dict = dict()

