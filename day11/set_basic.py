
# 집합(set)
# 순서가 없이 빠르게 저장, 중복저장 허용 X
names = {'허준', '신사임당', '권율', '홍길동', '허준'}
print(type(names))
print(len(names))
print(names)

for x in names:
    print(x)

# 빈 집합 만들기
s = set()
print(type(s))
print(s)

# set에 데이터 추가 / 삭제
asia = {'한국', '중국', '일본'}
print(asia)

asia.add('태국')
asia.add('중국')
print(asia)

asia.remove('일본')
print(asia)

# 결합(합집합) update함수
asia2 = {'이라크', '싱가포르', '한국'}
asia.update(asia2)
print(asia)