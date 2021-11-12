
import sys

# 메뉴데이터를 저장할 딕셔너리
# 저장 예시: {'짜장면': 4000, '짬뽕': 3000}
foods = {'짜장면': 4000, '짬뽕': 3000}


while True:

    print("\n\n====== 음식점 메뉴 관리 프로그램 ======")
    print("# 1. 신규 메뉴 등록하기")
    print("# 2. 메뉴판 전체보기")
    print("# 3. 프로그램 종료하기")
    print("=========================================")
    select = input("# 메뉴 입력: ")
    
    if select == '1':       
        while True: 
            food_name = input('- 메뉴명: ')

            if food_name not in foods:
                price = int(input('- 가격: '))
                # dict[new_key] = value
                foods[food_name] = price     
                break       
            else:
                print(f'# {food_name}은(는) 이미 등록된 메뉴입니다.')

    elif select == '2':        
        
        if len(foods) > 0:
            print('\n***** 메뉴판 *****')
            for f_name in foods:
                f_price = foods[f_name]
                print('# {:<3s}:{:>5d}원'.format(f_name, f_price))
            print('==================================')
            print('[ 1. 수정 | 2. 삭제 | 3. 나가기 ]')
            choice = int(input('>>> '))

            if choice == 1:
                m_name = input('# 수정할 메뉴명: ')
                if m_name in foods:
                    old_price = foods[m_name]
                    new_price = int(input(f'- 새로운 가격({old_price}): '))
                    # dict[key] = new_value 
                    foods[m_name] = new_price
                    print(f'\n# {m_name}의 가격이 {old_price}원에서 {new_price}원으로 변경되었습니다.')
                else:
                    print(f'{m_name}은(는) 등록된 메뉴가 아닙니다.')

            elif choice == 2:
                d_name = input('# 삭제할 메뉴명: ')
                if d_name in foods:
                    del(foods[d_name])
                    print(f'{d_name}이(가) 정상 삭제되었습니다.')
                else:
                    print(f'{d_name}은(는) 등록된 메뉴가 아닙니다.')
            else:
                continue

        else:
            print('\n# 메뉴를 먼저 등록하세요!')


    elif select == "3":
        print("# 프로그램을 종료하시겠습니까?[Y/N]")
        choice = input("=> ")
        if choice.lower()[0] == "y":
            print("프로그램을 종료합니다.")
            sys.exit()
        else:
            print("종료를 취소합니다.")
            continue
    else:
        print("메뉴를 잘못 입력했습니다.")

    input("\n메뉴를 보시려면 Enter....") 

