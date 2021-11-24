import sys
login_status = False

cafelist = [
    {'제품명' : '아메리카노',
    '가격' : 5000
    },
    {'제품명' : '카페라떼',
    '가격' : 4500
    }
]

user = []
    


# 함수 정의부

# 0 - 1_1 [회원가입] 함수 - 별명중복 
def check_duplicate_nickname():    
    while True:       
        info = input('- 별명: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if info == p['별명']:
                # 중복됨 
                print('중복되었습니다 다시 입력하세요')
                flag = True             
                break
        if flag == False:
            return info

# 0 - 1_2 [회원가입] 함수 - 아이디중복 
def check_duplicate_id():    
    while True:       
        info = input('- 아이디: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in user:
            if info == p['아이디']:
                # 중복됨 
                print('중복되었습니다 다시 입력하세요')
                flag = True             
                break
        if flag == False:
            return info            

# 0 - 1 [회원가입] 함수
def user_info():
    info = {}
    print('\n☆ 회원 가입을 시작합니다. ☆')      
    info['이름'] = input('- 이름: ')
    info['별명'] = check_duplicate_nickname()
    info['아이디'] = check_duplicate_id()
    if info['아이디'] not in user:
        print(' 사용가능 아이디 입니다')
    else:
        print('이미 등록된 아이디 입니다.')
    while True:     
        info['비밀번호'] = input('- 비밀번호: ')
        if info['비밀번호'] == input('- 비밀번호확인: '):
            user.append(info)
            print('회원가입 되셨습니다!')
            print('메뉴화면으로 돌아가시려면 Enter를 누르세요')
            input()
            return
        else:
            print('비밀번호가 일치하지 않습니다.')
            continue   
        
# 0 - 2 [로그인] 함수 
def login():
    print('----------로그인----------')
    # print(user)
    id = input('- 아이디: ')
    find_user = None
    for info in user:
        if (info['아이디'] == id):
            find_user = info
            break
    real_pw = find_user['비밀번호']
    pw = input('- 비밀번호: ')
    if real_pw == pw:
        print('로그인 되었습니다.')
        print('{}님 환영합니다.'.format(info['이름']))
        return True
    else:   
        print('비밀번호가 틀렸습니다.')
# 0 - 3_1 [id 찾기] - id 조회 헤드 함수
def header_id():
    print('\n\t\t*** 회원 아이디 조회 *** ')
    print('=' * 60)

# 0 - 3_2 [id 찾기] - 조회할 nickname 입력 문구 함수
def input_nickname(msg):
    print(f'# {msg}하실 별명을 입력하세요.')
    code = input('별명: ')
    return code  

# 0 - 3_3 [id 찾기] - 조회할 nickname 로테이션 함수
def get_nickname(code):
    for info in user:
        if code == info['별명']:
            return info
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴  

# 0 - 3 [id 찾기] 함수          
def search_id():
    code = input_nickname('조회')
    info = get_nickname(code)

    if len(info) > 0:
        header_id()
        print('[{:^7s}]님의 별명[{:^7s}], 아이디는 [{:^7s}]입니다.'.format(info['이름'], info['별명'], info['아이디']))
        print('=' * 60)
    else:
        print('# 존재하지 않는 아이디입니다.')   
    input()

# 0 - 4_1 [pw 찾기] = pw 조회 헤드 함수
def header_pw():
    print('\n\t\t\t*** 회원 비밀번호 조회 *** ')
    print('=' * 80)

# 0 - 4_2 [pw 찾기] = pw 조회할 name, id 입력 문구 함수
def input_name_id(msg):
    print(f'# {msg}하실 이름과 아이디를 입력하세요.')
    code = input('이름: ')
    return code

# 0 - 4_3 [pw 찾기] = pw 조회할 name, id 입력 로테이션 함수
def get_name_id(code):
    for info in user:
        if code == info['이름']:
            x = input('아이디: ')
            if info['아이디'] == x : 
                return info
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴

# 0 - 4 [pw 찾기] 함수
def search_pw():
    code = input_name_id('조회')
    info = get_name_id(code)

    if len(info) > 0:
        header_pw()
        print('[{:^7s}]님의 별명[{:^7s}],아이디는 [{:^7s}], 비밀번호는 [{:^7s}] 입니다.'.format(info['이름'], info['별명'], info['아이디'], info['비밀번호']))
        print('=' * 80)
    else:
        print('# 존재하지 않는 비밀번호입니다.')
    input()

# head 출력 함수
def show_menu():
    print('\n*** 어서오세요 카페입니다!! ***')
    print('# 1. 모든 메뉴보기')
    print('# 2. 개인정보 수정')
    print('# 3. 관리자 전용')
    print('# 4. 프로그램 종료하기')

# 1. [모든 메뉴보기] 출력 함수
def all_menu():
    print('\n***** 카페 전체 메뉴 *****')
    print('=' * 30)
    print('{:^8s}    {:^12s}'.format('제품명', '가격',))
    print('=' * 30)
    for menu in cafelist: 
        print('{}    {:>8d}원'.format(menu['제품명'], menu['가격']))
    print('=' * 30)
    
# 제품코드를 입력받는 함수
def input_code(msg):
    print(f'# {msg}하실 제품의 이름을 입력하세요')
    name = input('>> ')
    return name

# 제품번호로 해당 제품을 찾아오는 함수
def get_product(name):
    for menu in cafelist:
        if name == menu['제품명']:
            return menu
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴


# 2 - 1_1 [개인정보 수정] - id 입력 함수
def input_id(msg):
    print(f'# {msg}하실 아이디를 입력하세요.')
    code = input('아이디: ')
    return code

# 2 - 1_2 [개인정보 수정] - id 입력 로테이션 함수
def get_id(code):
    for info in user:
        if code == info['아이디']:
            return info
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴    

# 2. [개인정보 수정] 함수
def modify_privercy():
    code = input_id('수정')
    info = get_id(code)
    if len(info) > 0:
        print('\n# [{}] {}님의 정보를 수정합니다.'.format(info['별명'], info['이름'] ))
        info['아이디']
        print('[ 1. 별명 변경 | 2. 비밀번호 변경 | 3. 취소 ]')
        select = int(input('>> '))
        if select == 1:
            info['별명'] = input('-수정할 별명({}): '.format(info['별명']))
            print('별명이 수정되었습니다.')  
        elif select == 2:
            info['비밀번호'] = input('-수정할 비밀번호({}): '.format(info['비밀번호']))
            print('비밀번호가 수정되었습니다.')  
        else:
            print('# 변경을 취소합니다.')
    else:
        print('# 존재하지 않는 아이디입니다.')

# [관리자전용] head 함수
def show_manager():
    print('== 관리자 전용 ==')
    print('# 1. 메뉴 등록하기')
    print('# 2. 메뉴 수정하기')
    print('# 3. 메뉴 삭제하기')
    print('# 4. 취소')
    
# [관리자전용] 제품명 중복 확인 함수
def check_duplicate_manager():    
    while True:       
        name = input('- 제품명: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in cafelist:
            if name == p['제품명']:
                # 중복됨
                print('# 제품 이름이 중복되었습니다. 다시 입력하세요!')   
                flag = True             
                break
        if flag == False:
            return name

# [관리자전용] 메뉴 등록 함수
def make_menu():
    menu = {}
    print('\n메뉴 등록을 시작합니다!')
    menu['제품명'] = check_duplicate_manager()
    menu['가격'] = int(input('- 가격: '))
    cafelist.append(menu)
    print('메뉴 등록 완료!')

# [관리자전용] 메뉴 수정 처리 함수       
def modify_product():
    name = input_code('수정')
    menu = get_product(name)

    if len(menu) > 0:
        print('\n# {}의 정보를 수정합니다.'.format(menu['제품명']))
        menu['제품명']
        print('[ 1. 이름 변경 | 2. 단가 변경 | 3. 일괄 변경 | 4. 취소 ]')
        select = int(input('>> '))
        if select == 1:
            # 딕셔너리 수정: 딕셔너리변수[key] = new_value
            menu['제품명'] = input('- 수정할 이름({}): '.format(menu['제품명']))
        elif select == 2:
            menu['가격'] = int(input('- 수정할 가격({}): '.format(menu['가격'])))
        elif select == 3:
            menu['제품명'] = (input('- 수정할 이름({}): '.format(menu['제품명'])))
            menu['가격'] = int(input('- 수정할 가격({}): '.format(menu['가격'])))
        else:
            print('# 변경을 취소합니다.')
            input()
        print('수정이 완료되었습니다.')

    else:
        print('# 존재하지 않는 제품입니다.')
 
# [관리자전용] 메뉴 삭제 함수
def delete_product():
    code = input_code('삭제')
    menu = get_product(code)

    if len(menu) > 0:
        cafelist.remove(menu)
        print('\n# 제품이 정상 삭제되었습니다.')
    else:
        print('# 존재하지 않는 제품입니다.')

# 3. [관리자전용] 전체 함수
def manager_page():
    show_manager()
    select = int(input('=> '))

    if select == 1:
        make_menu()
    elif select == 2:
        modify_product()
    elif select == 3:
        delete_product()
    elif select == 4:
        print('취소합니다.')
    else:
        print('제대로 입력해주세요.')

# 4. [프로그램 종료] 함수
def exit_program():
    import sys
    print('\n# 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower() == 'y':
        sys.exit()
    else:
        print('종료를 취소합니다.')
        return

if __name__ == '__main__':
    
    while True:
        if login_status == False:
            print('로그인이 필요한 서비스입니다.')
            print('[ 1. 회원가입 || 2. 로그인 || 3. id 찾기 || 4. pw 찾기 ]')
            select = int(input('=> '))
            if select == 1:
                user_info()
            elif select == 2:
                login_status = login()
            elif select == 3:
                search_id()
            elif select == 4:
                search_pw()
        else:
            while True:   
                print(user)
                show_menu()
                select = int(input('=> '))
                if select == 1:
                    all_menu()
                elif select == 2:
                    modify_privercy()       
                elif select == 3:
                    manager_page()
                elif select == 4:
                    exit_program()
                else:
                    print('# 메뉴를 잘못 입력했습니다.')

                input()