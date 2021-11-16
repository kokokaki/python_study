
def hello(lang='한국어'):
    if lang == '한국어':
        print('안녕~')
    elif lang == '영어':
        print('hi!!')
    elif lang == '중국어':
        print('니하오')


def calc_stepsum(begin, end, step=1):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

###########################################

hello('영어')

# positional argument : 위치 인수 - 순서대로 전달되는 개념
print(calc_stepsum(1, 10, 1))
print(calc_stepsum(1, 10, 2))
print(calc_stepsum(1, 10))

# keyword argument : 키워드 인수 - 매개변수 이름으로 매칭
print(calc_stepsum(step=2, begin=3, end=6))

# 위치인수와 키워드인수의 혼합사용
print(calc_stepsum(1, step=1, end=5))


dog = '멍멍이'
cat = '야옹이'
print(dog, cat, sep='와', end='!!\n')
print(dog, cat, end='!!\n', sep='와')



