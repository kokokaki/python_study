
# 상품 재고관리 프로그램
# 상품 정보: [제품번호, 제품명, 가격, 수량, 총액]

product1 = {
    '제품번호': 'a001',
    '제품명': '냉장고',
    '가격': 500000,
    '수량': 4,
    '총액': 2000000
}
product2 = {
    '제품번호': 'a002',
    '제품명': '에어컨',
    '가격': 700000,
    '수량': 6,
    '총액': 4200000
}
product3 = {
    '제품번호': 'a003',
    '제품명': '냉장고',
    '가격': 1000000,
    '수량': 3,
    '총액': 3000000
}

print(product2['제품명'])
print(product1['가격'])

print('=' * 40)

inventory = [product1, product2, product3]

for product in inventory:
    print(product['제품명'])

print(inventory[2]['총액'])
print(product3 == inventory[2])

print('=' * 40)

code = input('# 제품 번호를 입력: ')

find_product = None
for product in inventory:
    if code == product['제품번호']:
        find_product = product
        break

if find_product != None:
    print('검색하신 제품의 이름은 {}입니다.'.format(find_product['제품명']))
else:
    print('해당 제품은 등록되지 않았습니다.')
