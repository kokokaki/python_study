import random

print('~~~~~~~ 재미있는 사칙연산 게임 ~~~~~~~~')
print('[즐겁게 문제를 푸시다가 지겨우면 0을 누르세요~]')
print('==============================================')

# 난이도 설정
print('======= # 게임의 난이도를 선택하세요!! =========')
print(' [ 1. 상 (1~100) | 2. 중 (1~50) | 3. 하 (1~20) ]')
level = int(input('>>> '))

if level == 1:
    levelNum = 100
elif level == 2:
    levelNum = 50
elif level == 3:
    levelNum = 20
else:
    levelNum = 999

qNum = 1
ok = 0 # 정답 횟수
no = 0 # 틀린 횟수

while True:
    first = random.randint(1, levelNum)
    second = random.randint(1, levelNum)

    # 연산기호를 결정할 랜덤 숫자 생성
    markNum = random.randint(1, 3)

    if markNum == 1:
        mark = '+'
        real = first + second
    elif markNum == 2:
        if first == second:
            second -= 1
        mark = '-'
        real = first - second
    else:
        mark = 'x'
        real = first * second

    print(f'\nQ{qNum}. {first} {mark} {second} = ??')
    qNum += 1 

    # 사용자의 입력값
    answer = int(input('>> '))

    # 종료 조건
    if answer == 0:
        print('게임을 종료합니다!')
        print('-------------------------------------')
        print(f'정답횟수: {ok}회, 틀린횟수: {no}회')
        break

    if real == answer:
        print('정답입니다!!')
        ok += 1
    else:
        print('틀렸어요~~')
        no += 1
