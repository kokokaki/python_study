
    




'''
* 연습
1. 인수를 정수형태로 시작값(start), 끝값(end)을 입력받아 
   반복문으로 start부터 end까지의 누적 총합을 구하는 함수를 
   정의하세요.
2. 함수 이름은 calc_rangesum로 정의하세요.
ex) calc_rangesum(3, 7) ==> 3부터 7까지의 누적합을 구해와야 함.
3. 출력예시: "x~y까지의 누적합: z"
'''

# 함수 정의
def calc_rangesum(start, end):
    total = 0
    for n in range(start, end + 1):
        total += n
    return total

# 함수 호출
print("-" * 40)
n1 = int(input("정수1: "))
n2 = int(input("정수2: "))

sum = calc_rangesum(n1, n2)
print(f"{n1}~{n2}까지의 누적합: {sum}")

