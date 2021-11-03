

a = 5

if (a > 1) and (a < 10):
    print('a는 1과 10사이의 정수입니다.')
else:
    print('a는 1과 10사이의 정수가 아닙니다.')
    

print('=' * 40)

b = 3
if (b == 2) or (b == 4):
    print('b는 2또는 4입니다.')
else:
    print('b는 2또는 4가 아닙니다.')


# not: 부정 (t->f ,  f->t)

d = 5

if d < 0:
    print('d는 0보다 작습니다.')

if not d < 0:
    print('d는 0보다 작지 않습니다.')

# c언어에서는 0을 false로 취급합니다. 
# 0이 아닌 모든 숫자를 true로 취급합니다.
apple = 0

if not apple:
    print('사과가 하나도 없어요!')
else:
    print(f'사과가 {apple}개 있어요!')