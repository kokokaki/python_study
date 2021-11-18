# 전역변수 정의부
inventory = [
    {
        '제품번호': 'a001',
        '제품명': '에어컨',
        '가격': 500000,
        '수량': 3,
        '총액': 1500000
    },
    {
        '제품번호': 'a002',
        '제품명': '세탁기',
        '가격': 800000,
        '수량': 7,
        '총액': 5600000
    },
    {
        '제품번호': 'a003',
        '제품명': '청소기',
        '가격': 120000,
        '수량': 7,
        '총액': 840000
    }
]
# 함수 정의부

# 메뉴를 출력하는 함수
def show_menu():
    print('\n*** 재고관리 프로그램 ***')
    print('# 1. 제품 정보 등록하기')
    print('# 2. 모든 제품정보 조회')
    print('# 3. 개별 제품정보 조회')
    print('# 4. 제품정보 수정하기')
    print('# 5. 제품정보 삭제하기')
    print('# 6. 프로그램 종료하기')

# 제품번호의 중복을 확인하는 함수
def check_duplicate_code():    
    while True:       
        code = input('- 제품 번호: ')    
        flag = False  # 중복 플래그          
        # 중복 검증
        for p in inventory:
            if code == p['제품번호']:
                # 중복됨
                print('# 제품 번호가 중복되었습니다. 다시 입력하세요!')   
                flag = True             
                break
        if flag == False:
            return code

# 제품등록을 수행하는 함수
def insert_product():
    product = {}
    print('\n# 제품 정보 등록을 시작합니다.')    
    
    product['제품번호'] = check_duplicate_code()
    product['제품명'] = input('- 제품명: ')
    product['가격'] = int(input('- 가격: '))
    product['수량'] = int(input('- 수량: '))
    product['총액'] = product['가격'] * product['수량']

    inventory.append(product)
    print('# 제품 등록 완료!')
    
# 프로그램 종료처리 함수
def exit_program():
    import sys
    print('\n# 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return


# 제품정보 출력 머리말 부분
def header_print():
    print('\n\t\t*** 창고 재고 정보 ***')
    print('=' * 55)
    print('{:^8s}{:^8s}{:^8s}{:^8s}{:^10s}'.format('제품번호', '제품명', '가격', '수량', '제품총액'))
    print('=' * 55)

# 전체 제품정보를 출력하는 함수
def print_all_products():
    header_print()

    total_price = 0
    for product in inventory:
        total_price += product['총액']
        print('{:^10s}{:^10s}{:>8d}원{:>6d}개{:>12d}원'.format(product['제품번호'], product['제품명'], product['가격'], product['수량'], product['총액']))
    print('=' * 55)
    print(f'\t\t창고 전체 재고 총액: {total_price}원')

# 제품코드를 입력받는 함수
def input_code(msg):
    print(f'# {msg}하실 제품의 번호를 입력하세요')
    code = input('>> ')
    return code

# 제품번호로 해당 제품을 찾아오는 함수
def get_product(code):
    for product in inventory:
        if code == product['제품번호']:
            return product
    return {} # 못 찾을 경우 상징적으로 빈 딕셔너리 리턴

# 개별 제품 조회 처리 함수
def search_product():
    code = input_code('조회')
    product = get_product(code)
    
    if len(product) > 0:
        header_print()
        print('{:^10s}{:^10s}{:>8d}원{:>6d}개{:>12d}원'.format(product['제품번호'], product['제품명'], product['가격'], product['수량'], product['총액']))
    else:
        print('# 존재하지 않는 제품입니다.')

# 제품정보 수정 처리 함수
def modify_product():
    code = input_code('수정')
    product = get_product(code)

# 제품정보 삭제 처리 함수
def delete_product():
    code = input_code('삭제')
    product = get_product(code)
    


# 메인 실행부
if __name__ == '__main__':
    
    while True:
        show_menu()
        menu = int(input('>> '))
        
        if menu == 1:
            insert_product()
        elif menu == 2:
            print_all_products()
        elif menu == 3:
            search_product()
        elif menu == 4:
            modify_product()
        elif menu == 5:
            delete_product()
        elif menu == 6:
            exit_program()
        else:
            print('# 메뉴를 잘못 입력했습니다.')

        input('\n# Enter를 누르시면 메뉴로 돌아갑니다.')

