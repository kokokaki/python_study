

# docstring: 함수의 설명서 
# help() - docstring 열람
help(print)

print('=' * 40)

help(len)

def calc_sum(start, end):
    '''
    # calc_sum 함수는 범위의 정수를 2개 입력하면
      해당 범위의 총합을 구해서 리턴합니다.
    
    * 매개변수 
    1. start: 시작값을 의미합니다. 시작값은 계산에 포함됩니다.
    2. end: 끝값을 의미합니다. 끝값도 계산에 포함됩니다.

    * 반환값
    - 범위의 누적 총합을 반환합니다.
    '''
    sum = 0
    for n in range(start, end+1):
        sum += n
    return sum

print('=' * 40)
help(calc_sum)