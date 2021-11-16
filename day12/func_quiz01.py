
# 함수 정의부
def min2(first, second):
    if first > second:
        return second
    else:
        return first

# 실행부
if __name__ == '__main__':

    print('정수 2개를 입력하세요!')
    n1 = int(input('정수 1: '))
    n2 = int(input('정수 2: '))

    print(f'두 숫자 중에 작은 수는 {min2(n1, n2)}입니다.')