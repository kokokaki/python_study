
level = int(input('구구단 단수: ')) # 단수

print(f'구구단 {level}단')
print('===============')

n = 1
while n <= 9:
    print(f'{level} x {n} = {level * n}')
    n += 1

'''
for n in range(1, 10):
    print(f'{level} x {n} = {level * n}')
'''