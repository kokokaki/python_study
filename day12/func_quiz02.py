
# 함수 정의부
def min3(first, second, third):
    min_value = first # 최소값을 저장해둘 변수
    if second < min_value: min_value = second
    if third < min_value: min_value = third
    return min_value

def min3_v2(first, second, third):
    numbers = [first, second, third]
    return min(numbers)

# 실행부
if __name__ == '__main__':

    print('정수 3개를 입력하세요!')
    n1 = int(input('정수 1: '))
    n2 = int(input('정수 2: '))
    n3 = int(input('정수 3: '))

    print(f'세 숫자 중에 가장 작은 수는 {min3(n1, n2, n3)}입니다.')