

# split함수는 구분자를 기준으로 문자열을 분할하여
# 리스트에 담아서 반환함.

s1 = '닭강정 김말이 떡볶이'
foods = s1.split() # 구분자의 기본값은 공백
print(foods)

s2 = '서울->대전->대구->부산'
city = s2.split('->')
print(city)


s3 = '홍길동 | 오렌지출판사 | 2020년 8월'
book_data = s3.split('|')
print(book_data)

