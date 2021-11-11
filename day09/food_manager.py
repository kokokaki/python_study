
import sys

# 메뉴데이터를 저장할 딕셔너리
# 저장 예시: {'짜장면': 4000, '짬뽕': 3000}
foods = {}

while True:

    print("\n\n====== 음식점 메뉴 관리 프로그램 ======")
    print("# 1. 신규 메뉴 등록하기")
    print("# 2. 메뉴판 전체보기")
    print("# 3. 프로그램 종료하기")
    print("=========================================")
    select = input("# 메뉴 입력: ")
    if select == '1':        
        pass
    elif select == '2':        
        pass
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

