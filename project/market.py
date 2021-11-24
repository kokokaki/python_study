import os
import pickle


# 중고나라 마켓 만들기
# ID  PW  성별  주소  전화번호
# 제목 이름 작성자 상태 가격

#dir_name = "D:/isce_yeon/py_study"
#file_name = "junggo_market_sav"


all_id = [
    {"ID" : "showme", "PW" :"1234", "성별" : "남", "주소" : "대전", "전화번호" : "01012121212"},
    {"ID" : "badboi", "PW" :"5678", "성별" : "여", "주소" : "대전", "전화번호" : "01034343434"},
    {"ID" : "choco", "PW" :"9090", "성별" : "여", "주소" : "부산", "전화번호" : "01056565656"}
    ]

all_goods = [
    {"제목" : "오늘까지팜", "이름" : "텀블러", "작성자":"이철수", "상태" : "거의 새거", "가격" : 30000},
    {"제목" : "내일까지팜", "이름" : "폰케이스", "작성자":"김철수", "상태" : "쫌 씀", "가격" : 5000},
    {"제목" : "떨이함", "이름" : "문상50000", "작성자":"박철수", "상태" : "새거", "가격" : 10000},
]

# 현재 로그인한 사람 정보
current_login_user = None


# 세이브 생성
'''
def save_market():
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    try:
        f = open(dir_name+file_name, "wb")
        pickle.dump(all_id, f)
        pickle.dump(all_goods, f)
        
    except:
        print("파일 저장 실패 ㅠㅠ")
    finally:
        f.close()


# 파일 로드
def load_market():
    global all_id
    global all_goods

    try:
        f = open(dir_name+file_name, "rb")
        all_id = pickle.load(f)
        all_goods = pickle.load(f)
    except:
        print("파일 로드 실패 ㅠㅠ")
    finally:
        f.close()
'''
# 메인
def show_main():
    while True:
        print("="*55)
        print("\t\t***** isec 마켓 *****")
        print("="*55)
        print("\t 【isec 마켓】 에 오신걸 환영합니다")

        print("\n\t\t--------------- menu ---------------")
        print("1. 로그인  | 2. 회원가입  |  3. 종료")
        choice = int(input(">> "))
        if choice == 1:
            login_id_pw()

        elif choice == 2:
            join_id()

        elif choice == 3:
            exit_program()
        
        else:
            print("잘못 입력하셨습니다. 다시 선택해주세요 !")
            continue
        break


# 로그인 이후 메인
def show_login_main():
    print("\n------------------------------- main menu -------------------------------")
    print("[ 1. 공지사항  |  2. 제품판매  | 3. 제품구매  |  4. 회원정보  |  5. 종료 ]")


def login_id_pw():
    global current_login_user
    log_count = 0
    while True:
        if log_count == 3:
            print("-"*50)
            print("경고 !! 로그인 실패 횟수가 5회가 되면 강제종료됩니다.")
            print("-"*50)
        elif log_count > 4:
            print("-"*50)
            print("보안을 위해 로그인 시스템을 종료합니다.")
            print("-"*50)
            exit_baro()

        insert_id = input("ID :")
        insert_pw = input("PW :")

        find_user = None
        for n in all_id:
            
            if insert_id == n["ID"]: # 일치하는 ID가 있으면 find_user에 유저 정보를 저장
                find_user = n
                break

    
        if find_user == None: # 없는 ID를 입력하였을 때 continue를 통해 다시 ID 입력으로 이동
            print("ID를 잘못 입력하셨습니다. ")
            log_count += 1
            print("로그인 {}회 실패하셨습니다.".format(log_count))
            continue
         
        # 아이디는 잘 입력
        real_pw = find_user['PW']
        if real_pw == insert_pw:
            print("!! {}님 즐거운 쇼핑 되세요 !!" .format(insert_id)) # 비밀번호까지 잘 입력
            current_login_user = find_user
            return current_login_user
            
        else:
            print("비밀번호를 잘못 입력하셨습니다.") # 비밀번호를 잘못 입력하였을 때 continue를 통해 다시 입력으로 이동
            log_count += 1
            print("로그인 {}회 실패하셨습니다.".format(log_count))
            continue  
        

# 회원가입
def join_id():
    print("순서대로 기입해주세요 !")
    #print("다시는 수정할 수 없으니 주의해서 입력해 주시기 바랍니다 !!!!!!!!!")
    infor = {}
    while True:
        infor["ID"] = check_id()
        if len(infor["ID"]) < 5:
            print("ID는 5글자 이상으로 쓰세요.")
        else:
            print("사용 가능한 ID입니다.")
            break

    while True:
        infor["PW"] = input("PW : ")
        if len(infor["PW"]) < 4:
            print("PW는 4글자 이상으로 쓰세요.")
        else:
            print("사용 가능한 PW입니다.")
            break

    infor["성별"] = input("성별 : ")
    infor["주소"] = input("주소 : ")
    infor["전화번호"] = input("전화번호 : ")

    print("회원가입이 완료되었습니다.")
    all_id.append(infor)
    login_id_pw()
    #save_market()

# 회원 중복체크
def check_id():
    while True:
        code = input("id : ")
        flag = False

        for p in all_id:
            if code == p["ID"]:
                print("# ID 가 중복되었습니다. 다시 입력하세요!")
                flag = True
                break
        
        if flag == False:
            return code


# 회원정보 찾기 입력
def my_id_infor():
    print("# 수정하실 회원님의 ID를 입력해주세요")
    code = input(">> ")
    return code


# 회원정보 가져오기
def get_id_infor(code):
    for infor in all_id:
        if code == infor["ID"]:
            return infor
    return {}


# 회원정보출력머리
def head_id_infor():
    print("="*50)
    print("{} 님의 회원정보 입니다.".format(current_login_user["ID"]) )
    print("="*50)
    print("ID     PW     성별     주소     전화번호")
    print("="*50)
    print("{}\t{}\t{}\t{}\t{}" .format(current_login_user["ID"], current_login_user["PW"], current_login_user["성별"], current_login_user["주소"], current_login_user["전화번호"]))
    print("="*50)

# 회원정보출력
def id_infor():
    head_id_infor()


# 회원 정보 수정
def id_append():
    print("[0. 회원정보 | 1. 비밀번호 수정 | 2. 주소 수정 | 3. 전화번호 수정 | 4 . 회원 탈퇴]")
    choice = int(input("번호를 선택하세요 >> "))
    
    if choice == 0:
        id_infor()

    elif choice == 1:
        print("비밀번호를 수정합니다.")
        before_pw = current_login_user["PW"]
        after_pw = input("수정하실 비밀번호를 입력해주세요 >> ")
        current_login_user["PW"] = after_pw
        print("비밀번호가 {}에서 {}으로 변경되었습니다. ".format(before_pw, after_pw))

    elif choice == 2:
        print("주소를 수정합니다.")
        before_ad = current_login_user["주소"]
        after_ad = input("수정하실 주소를 입력해주세요 >> ")
        current_login_user["주소"] = after_ad
        print("주소가 {}에서 {}으로 변경되었습니다. ".format(before_ad, after_ad))
    
    elif choice == 3:
        print("전화번호를 수정합니다.")
        before_num = current_login_user["전화번호"]
        after_num = input("수정하실 전화번호를 입력해주세요 >> ")
        current_login_user["전화번호"] = after_num
        print("전화번호가 {}에서 {}으로 변경되었습니다. ".format(before_num, after_num))

    elif choice == 4:
        delete_id()
    #save_market()
        

# 회원탈퇴
def delete_id():

    user_del = input("정말로 탈퇴하시겠습니까 ? [Y/N]\n")
    
    if user_del.lower() == "y":
        print("정상적으로 탈퇴되었습니다.")
        all_id.remove(current_login_user)
        show_main()
        #save_market()

    else:
        print("탈퇴가 취소되었습니다 .\n")



# 제품판매
def insert_goods():
    goods_infor = {}
    print("="*55)
    print("순서대로 기입해주세요 !")
    goods_infor["제목"] = input("제목 : ")
    goods_infor["이름"] = input("이름 : ")
    goods_infor["작성자"] = input("작성자 : ")
    goods_infor["상태"] = input("상태 : ")
    goods_infor["가격"] = input("가격 : ")
    
    print("물건 등록이 완료되었습니다")
    all_goods.append(goods_infor)
    #save_market()
    pan_goods()


# 제품구매 선택
def pan_goods():
    print("="*55)
    print("[ 1. 제품등록  |  2. 제품삭제  |  3. 뒤로가기]")
    print("="*55)

    choice = int(input("선택하세요 >> "))

    if choice == 1:
        insert_goods()
        
    elif choice == 2:
        product_change()

    elif choice == 3:
        print()

    else:
        print("다시 선택하세요")
        

# 제품구매
def sell():
    print("="*55)
    print("\t\t-----거래 게시판-----")
    print("="*55)
    list_hall()

    goods = None
    sell_goods = input("구매하실 제품의 이름을 기입해주세요. \n")
    for n in all_goods:

        if sell_goods == n["이름"]:
            goods = n
            
            print("판매자인 {}님에게 문의를 하시겠습니까? [Y/N]" .format(n["작성자"]))
            talk = input("=> ")
            if talk.lower()[0] == 'y':
                print("{}님께 글을 남겨보세요!".format(n["작성자"]))
                print("-"*50)
                talk = input("=> ")
                print("{}님께 '{}'라고 남기셨습니다." .format(n["작성자"], talk))
                print("-"*50)
                print("판매자인 {}님의 제품인 {}을 구매하시겠습니까? [Y/N]" .format(n["작성자"], n["이름"]))
                buy = input("=> ")
                if buy.lower()[0] == 'y':
                    all_goods.remove(goods)
                    print(f"{sell_goods} 상품의 구매가 완료되었습니다. ")
                    break   
                elif buy.lower()[0] == 'n':
                    print("아님 말고..")
                    print()            
                    
            else :
                print("판매자인 {}님의 제품인 {}을 구매하시겠습니까? [Y/N]" .format(n["작성자"], n["이름"]))
                buy = input("=> ")
                if buy.lower()[0] == 'y':
                    all_goods.remove(goods)
                    print(f"{sell_goods} 상품의 구매가 완료되었습니다. ")
                    break   
                elif buy.lower()[0] == 'n':
                    print("아님 말고..")
                    print()
    #save_market()

        if sell_goods != n["이름"] and buy.lower()[0] != 'y' and buy.lower()[0] != 'n':
            print("잘못된 이름입니다. 다시 기입해주세요. ")
        

# 거래게시판 리스트
def list_hall():
    num = 0
    master_user = None
    print("순서\t제목\t\t이름\t\t작성자")
    print("="*50)
    for pan in all_goods:
        num += 1
        print("\n{}.{:^8s}\t{:^11s}\t{:>10s}" . format(num, pan["제목"], pan["이름"],pan["작성자"]))
    print("="*50)


# 제품삭제
def product_change():

    print("="*55)
    print("\t\t-----거래 게시판-----")
    print("="*55)
    list_hall()

    goods = None
    del_goods = input("삭제하실 제품의 이름을 기입해주세요. \n")
    for n in all_goods:

        if del_goods == n["이름"]:
            goods = n
                
            print("{} 를 정말로 삭제하시겠습니까 ? [Y/N]" .format(n["이름"]))
            good_del = input("=> ")
            if good_del.lower()[0] == 'y':
                all_goods.remove(goods)
                print(f"{del_goods} 상품의 삭제가 완료되었습니다. ")
                #save_market()
                break

            elif good_del.lower()[0] == 'n':
                print("상품의 삭제가 취소되었습니다. ")
                break
                        
            else:
                print("다시 입력해주세요.")
                continue
            

# 공지사항
def gongzi():
    print("="*55)
    print("\t\t -- 사이트 공지사항 --")
    print("="*55)

    print("> 이곳은 isec 마켓으로\n공정한 거래를 지향합니다.")
    print("\n> 불공정 거래로 인한 신고가 발생 시\n확인 후 제재 조치 취하겠습니다.")
    print("\n> 2021.11.27 ~ 2021.11.30 까지\n블랙프라이데이 이벤트 진행예정")
    print("\n> 2021.12.25 단하루 !!\n선착순 100명에게 50% 할인 쿠폰 지급 !!")
    print()
    show_login_main()
    

# 종료
def exit_program():
    import sys
    print("# 프로그램을 종료합니다. [Y/N]")
    end = input("=> ")
    if end.lower()[0] == "y":
        print("다음에 또 들려주세요 !!")
        sys.exit()
    else:
        print("탁월한 선택 !! 아직 물건은 많아요 !!\n")
        return

# 바로 종료
def exit_baro():
    import sys
    print("# 프로그램을 종료합니다.")
    sys.exit()


if __name__ == '__main__':

    # load_market()  # 세이브 이후에 실행

    show_main()

    while True:
        show_login_main()
        select = int(input("선택해주세요 >> "))

        if select == 1:
            gongzi()

        elif select == 2:
            pan_goods()

        elif select == 3:
            sell()

        elif select == 4:
            id_append()

        elif select == 5:
            exit_program()

        else:
            print("다시 선택해주세요")

        input("\n# 메뉴화면으로 돌아가시려면 Enter를 누르세요.")