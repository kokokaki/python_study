
n1 = 10
result = n1 + 20
print(result * 3)

result = result + 3
print(result)

# 선언(make)되지 않은 변수는 사용 불가!
# result = number + 10 
# print(number)
print("number")  # 따옴표안에 있으면 전부 텍스트로 취급(변수 X)

fruit = '사과'

print(fruit + ' 맛있어요~')

print('=================================')

# 변수 이름 규칙

# 1. 숫자로 시작하면 안됨
# 7number = 700
number7 = 700
num7ber = 777

# 2. 공백을 포함할 수 없음
# user birth day = 19940101
userbirthday = 19940101

user_birth_day = 19940101 # snake case (파이썬 선호)
userBirthDay = 19940101   # camel case (자바, 자바스크립트 선호)

# 3. 대/소문자를 구분함
banana = '바나나'
BANANA = '뻐네이너'
print(BANANA)

# 4. if, while과 같은 이미 기능이 포함된 단어는 변수이름 사용불가!
# if = 123
# for = "메롱"
whilE = 123

# 한글, 한자변수 가능? - 가능하지만 안쓰는걸 권고
야옹이 = '고양이'
print(야옹이)

# print()와 같은 내장함수의 이름은 변수이름으로 지정가능하나
# 그 본래기능을 더이상 활용할 수 없습니다.
# print = 500
# print();


# 다중 변수 선언
# a = 10
# b = 20
a, b = 10, 20;
print(a + b)

