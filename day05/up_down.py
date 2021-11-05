import random

# 게임의 정답: 1 ~ 100사이의 랜덤 정수
secret = random.randint(1, 100)

print('[UP & DOWN 게임 - 1 ~ 100사이의 무작위 숫자를 맞춰보세요!]')

min = 1
max = 100
count = 0
count_down = 6

# 난이도 설정
print('# 게임의 난이도를 선택하세요!! ')
print(' [ 1. 상 | 2. 중 | 3. 하 ]')
level = int(input('>>> '))

if level == 1:
    print('난이도 상을 선택했습니다. 기회가 4번 주어집니다.')
    count_down = 4
elif level == 2:
    print('난이도 중을 선택했습니다. 기회가 6번 주어집니다.')
    count_down = 6
elif level == 3:
    print('난이도 하를 선택했습니다. 기회가 8번 주어집니다.')
    count_down = 8
else:
    print('난이도 선택이 잘못되었으므로 상난이도로 자동시작합니다.')
    count_down = 4

while True:  

    # 카운트다운이 소진되었을 시점에 알림메시지 제공
    if count_down == 0:
        print('승리 기회가 날아갔습니다. 그러나 문제를 계속 풀어주세요!')

    # 사용자의 입력
    if count_down > 0:
        answer = int(input(f'\n# 숫자를 입력하세요({min} ~ {max} | {count_down}): ')) 
    else:
        answer = int(input(f'\n# 숫자를 입력하세요({min} ~ {max}): '))   


    # 범위 안의 값을 입력했는지 검증
    if (min > answer) or (max < answer):
        print('\n# 범위를 벗어난 값을 입력했습니다.')
        continue

    # 입력카운트 증가
    count += 1
    count_down -= 1

    if secret == answer:
        print(f'정답입니다!! {count}번만에 맞추셨네요!')
        if count_down >= 0:
            print('YOU WIN!!')
        else:
            print('YOU LOSE!!')
        break
    elif secret > answer:
        print('UP!!!')
        min = answer
    else:
        print('DOWN!!!')
        max = answer


