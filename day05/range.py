
'''
* 내장함수 range()

- 순차적으로 증가하는 정수의 리스트를 만들 때 
 대괄호 안에 데이터들을 콤마로 일일히 나열하기보다는
 range함수를 사용하여 쉽게 순차형 리스트를 만들 수 있습니다.

 ex) range(begin, end, step)
 - begin은 포함 , end는 미포함 (이상 미만 개념)
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

list2 = list(range(1, 11, 1))
print(list2)

# 마지막 값 생략시 자동으로 1로 처리
list3 = list(range(1, 11))
print(list3)

list4 = list(range(1, 11, 2))
print(list4)

# 값을 한개만 주면 end값으로 처리 begin을 0으로 처리
# range(5) == range(0, 5, 1)
list5 = list(range(5))
print(list5)
