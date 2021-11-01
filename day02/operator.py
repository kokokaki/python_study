
# 산술연산자
a, b = 18, 4
print(a / b)
print(a // b)
print(a % b)

# 4 % 10  -> 몫:0, 나머지: 4 // 앞숫자가 더작으면 앞이 나머지
# 0 % 7   -> 몫:0, 나머지: 0
# 7 % 0   -> 연산불가 : 에러발생

print(3 ** 2) 
print(2 ** 4)



# 복합대입 연산자
print('============================')

a = 5

a += 1 # a = a + 1
print(a)

a -= 2
print(a)

a *= 3 
print(a)

a //= 5
print(a)

a **= 5
print(a)

a =+ 20
print(a)

# 선언되지 않은 변수는 복합대입을 사용할 수 없습니다.
# c += 2 # c = c + 2


# 관계 연산자
print('=========================')
d = 5
print(d < 6)
print(d >= 10)
print(d == 5)

e = d == 7 - 2
print(e)
print(type(e))

# 문자열 비교
print('====================')

# 사전에서 앞에나오는 단어가 작다
print('ace' < 'ade')
print('apple' < 'grape')
print('zebra' < '감자')
print('짜장면' < '김밥')

password = 'abc1234'
print(password == 'ABC1234')

# 문자열 특수 연산
s1 = '메롱'
print(s1 * 3)
print('=' * 40)

# print(s1 * 1.5)
# print(s1 * '메롱')
