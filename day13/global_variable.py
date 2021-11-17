
sale_rate = 0.8  # 전역 변수

def calc_price(price):
    today_price = price * sale_rate
    print(f'오늘의 가격: {today_price}원')

print(sale_rate)
# print(today_price)
# print(price)

# 전역변수의 수정으로 인해 함수 실행결과가 바뀔 수 있다.
sale_rate = 0.6

calc_price(2000)



money = 1000  # 전역 변수

def discount():
    # 함수를 통해 전역변수 값에 관여하려면 global 키워드를 사용
    global money  # 앞으로 이 함수에서는 전역변수 money를 활용해라

    print('함수 discount 실행!')
    money = 500  # 지역 변수
    # 함수 내부에서는 지역변수가 우선
    print(f'지역변수 money : {money}')
    print(f'지역변수 money의 메모리주소값: {hex(id(money))}')

discount()

print(f'전역변수 money: {money}')
print(f'전역변수 money의 메모리주소값: {hex(id(money))}')


