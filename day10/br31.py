
import sys


# 플레이어들의 이름을 저장할 리스트
player_list = []

# 플레이들의 입력 숫자를 누적저장할 리스트
thirty_one_list = []

print('### 베스킨 라빈스~~~ 써리 원~!')
print('- 참여인원을 입력(최소2 최대 4)')

while True:
    player_num = input('>>> ')

    # 숫자로 썼는지 검증
    if not player_num.isdecimal():
        print('# 숫자로 쓰라 했다~~~')
        continue
    else:
        player_num = int(player_num)

    if player_num < 2 or player_num > 4:
        print('인원 범위가 알맞지 않음!(2 ~ 4 입력)')
        continue


    # 인원은 일단 제대로 썼음
    print(f'\n# {player_num}명의 플레이어가 참여했습니다.')
    print('## 플레이어들의 닉네임을 등록합니다.')

    for i in range(player_num):
        while True:
            player_name = input(f'# {i+1}번 플레이어 이름: ')

            # 이름 검증
            # 1. 이름을 안적은 경우
            if len(player_name.strip()) == 0:
                print('# 필수 입력사항입니다.')
            # 2. 중복된 이름인 경우
            elif player_name in player_list:
                print('# 이미 등록된 이름입니다.')
            # 3. 나쁜 이름인 경우
            elif player_name in ['돌아이', '멍멍이', '빡대가리']:
                print('# 해당 이름은 사용할 수 없습니다.')
            else:
                player_list.append(player_name)
                break
    
    ###############################################################
    ## 게임 시작 ##
    turn = 0 # 현재 턴의 플레이어 인덱스를 저장
    start = 1 # 입력해야할 값을 안내하는 숫자
    while True:
        print(f'\n# {player_list[turn]}의 턴!!')

        if start >= 31:
            print(f'\n# {player_list[turn]} 패배!! GAME OVER!!')
            sys.exit()


        print("[ 숫자를 입력하세요(최소 1개, 최대 3개) | 예시: 23 24 25 ]")
        print("# 마지막에 31을 입력하는 플레이어가 패배합니다.")

        print(f'# 현재 {start}부터 입력하시면 됩니다!!')
        
        while True:
            answer_list = list(map(int, input('>>> ').split()))

            ### answer_list 검증
            if len(answer_list) <= 0:
                print('# 아무것도 입력하지 않았습니다! 다시 입력하세요!')
            elif len(answer_list) > 3:
                print('# 1개에서 3개 사이의 숫자를 입력하세요!')
            elif ((len(answer_list) == 2) and (answer_list[0] + 1 != answer_list[1])):
                print('# 순차적인 숫자를 입력하세요!')
            elif ((len(answer_list) == 3) and ((answer_list[0] + 1 != answer_list[1]) or (answer_list[1] + 1 != answer_list[2]))):
                print('# 순차적인 숫자를 입력하세요!')
            elif start != answer_list[0]:
                print(f'# 숫자를 {start}부터 제대로 입력하세요!')
            else:
                # 검증 완료 케이스
                thirty_one_list += answer_list

                # 턴 보정
                # 현재 턴이 마지막 플레이어였다면 다음 턴은 첫번째 플레이어로 보정
                if turn == len(player_list) - 1:
                    turn = 0
                else:
                    turn += 1

                # start값 보정
                start = thirty_one_list[-1] + 1

                break # 숫자 입력 마감
                

          
    