
students = {'멍멍이':'김철수', '야옹이':'도우너', '짹짹이':'마이콜'}
print(type(students))
print(len(students))

print(students['야옹이'])
# print(students['개굴이'])

# in 키워드를 통해 key값의 존재여부를 체크할 수 있음
print('멍멍이' in students)
print('까마귀' in students)

print('=' * 40)

nick = input('별명: ')

if nick in students:
    print(f'별명이 {nick}인 학생의 이름은 {students[nick]}입니다.')
else:
    print('그런 학생은 없습니다.')