
total = 0
for n in range(1, 6):
    total += n

print(f'1~5까지의 누적합: {total}')

############## 코드 400줄가량 더 쳤음 ################
total = 0
for n in range(1, 51):
    total += n

print(f'1~50까지의 누적합: {total}')


######################################################
total = 0
for n in range(1, 101):
    total += n

print(f'1~100까지의 누적합: {total}')


#############################################

# 함수의 정의 (1 ~ x까지의 총합을 구하는 함수)
def calc_total(x):
    print('함수 calc_total 실행*^^7')
    total = 0
    for n in range(1, x+1):
        total += n
    return total

print('#' * 50)

# 함수는 정의한것만으로는 실행되지 않음
# 반드시 호출을 통해 실행시켜야 함
num = calc_total(10)
print(f'1~10까지의 총합: {num}')


########## 코드를 10만줄 더 썻음 ###############

num = calc_total(100)
print(f'1~100까지의 총합: {num}')

num = calc_total(123)

print('-' * 40)

###############################

# len()함수 직접 구현
def length(list):
    count = 0
    for x in list:
        count += 1
    return count

n_list = [10, 40, 90, 100, 500]

sss = "hello!!!"

print(f'사용자 정의함수 length(n_list): {length(n_list)}')
print(f'파이썬 내장함수 len(n_list): {len(n_list)}')

print(f'사용자 정의함수 length(sss): {length(sss)}')
print(f'파이썬 내장함수 len(sss): {len(sss)}')
